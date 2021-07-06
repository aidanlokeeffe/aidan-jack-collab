'''
Okay, this is the big class. In this explanation, we will use concepts from the
Package and Container classes freely. 

An experiment should be thought of as the whole shebang. The setup, the 
simulation, and the analysis. Accordingly, there are several sections of
methods in this class file. At the time of writing this comment, those 
sections are:
* SETUP METHODS
* DYNAMIC METHODS
* DATA FORMATTING MATHODS
* OUTPUT METHODS

The SETUP methods set the initial conditions. There is a helper function that
reads in an adjacency matrix. Note that the adjacency matrix is then an 
attribute of an experiment. (A comment for Jack and myself: We may want to give 
the user a choice for using a csv or a 2-D array, since this will mesh better 
with the ensemble class).

There are two DYNAMIC function: advance and execute. advance takes a parameter 
t so it can pass it to Container.fill. advance goes to the time t+1, and
records all the attempted and actual activity, as well as the ages, and the 
deaths. execute iterates advance up to the user provided time horizon.

All of the DATA FORMATTING functions are helpers to the OUTPUT functions. I 
won't say too much on these here, as that part of the code is currently
undergoing a lot of changes.
'''


import numpy as np
import math
from Container import Container
from Package import Package

class Experiment(object):
    ##############################
    ##############################
    # SETUP METHODS
    ##############################
    ##############################

    # Constructor
    def __init__(self, fileName, load, T, choice=0):
        # Inputs
        self.load = load
        self.T = T
        self.input_matrix(fileName)
        self.choice = choice

        self.executed = False

        
        # Initialize dynamical variable
        self.state = Container(self.N)
        self.state.fill(0, self.load)
        
        # Results
        self.attempted = []
        self.actual = []
        self.ages = []
        self.deaths = []

        # Recordings related to extinction and visitation
        # Since there are no deaths at time 0, we know that each ID is extant
        self.extant = set( range(self.load) )
        
        # Likewise, there are no extinct messages at the first time step
        self.extinct = set()

        # This will be a dictionary. The keys will be IDs, and the values will
        # be dictionaries, who in turn have keys as times and values as 
        # sets of nodes visited
        self.ID_trajectories = {}

        self.node_hists = []
        

        # Record the initial conditions
        # For this time step only, we can use the presence of an ID to denote attempted activity
        self.attempted.append( [len(self.state.contents[j].vals[0]) for j in range(self.N)] )

        # On the first time step, attempted and actual are equal
        self.actual.append([len(self.state.contents[j].vals[0]) for j in range(self.N)]) 

        # Record ages
        self.ages.append([len(self.state.contents[j].vals[1]) for j in range(self.N)])
        
        # There are no deaths on the first time step         
        self.deaths.append([]) 

        # Record visits
        # Put a function "record_visits" here.
        # Also, this function will need to do something different, so just hold on man. Hold on

        # Since this is the initial condition, no messages have been spread
        # yet, so every ID is in one and only one place
        for j in range(self.N):
            num_tags = len(self.state.contents[j].vals[0])
            for k in range(num_tags):
                key = self.state.contents[j].vals[0][k]
                self.ID_trajectories[key] = {}
                self.ID_trajectories[key][0] = set(self.state.contents[j].vals[1][k])


        # Record the IDs present at each node, otherwise, put -1

        # Put a function "record_node_hists" here
        next_node_hist = []
        for j in range(self.N):
            try:
                next_node_hist.append( self.state.contents[j].vals[0][0] )
            except IndexError:
                next_node_hist.append(-1)
        self.node_hists.append( next_node_hist )
        
        # Apply user's choice of propagation function
        if choice==0:
            self.propagate = self.state.RW_propagate
        else:
            self.propagate = self.state.IS_propagate


    # Read the csv containing the adjacency matrix, and set a few more object attributes
    def input_matrix(self, inFile):
        matrix = np.genfromtxt(inFile, delimiter = ',')
        if math.isnan(matrix[0][0]):
            matrix = matrix[1:,1:]
        self.adj = matrix
        self.N = len(matrix)


    ##############################
    ##############################
    # DYNAMIC METHODS
    ##############################
    ##############################

    # This method takes the experiment forward one time step, and records all of the appropriate stuff to the class attributes
    def advance(self, t):
        # Propagate the messages according to the chosen rule
        self.propagate(self.adj)
        
        # Add the random messages after propagating
        new_message = Container(self.N)
        new_message.fill(t, self.load)
        self.state.incorporate(new_message)

        # Put all the new IDs in the list of extant IDs
        self.extant |= set( range(t*self.load, (t+1)*self.load) )


        # Record ID_trajectories
        # First, we need the current positions for each ID
        current_positions = {}
        for j in range(self.N):
            num_tags = len(self.state.contents[j].vals[0])
            for k in range(num_tags):
                key = self.state.contents[j].vals[0][k]
                try:
                    current_positions[key] |= set( self.state.contents[j].vals[1][k] )
                except KeyError:
                    current_positions[key] = set( self.state.contents[j].vals[1][k] )

        # Once we have all of the current positions for each ID, we can compare with the 
        # cumulative visits, and if there are any new nodes visited, we take note of that
        keys = current_positions.keys()
        for key in keys:
            try:
                prev_time = max( self.ID_trajectories[key].keys() )
            except KeyError:
                # This means that the ID is new, so we set
                self.ID_trajectories[key] = {}
                self.ID_trajectories[key][t] = current_positions[key]
                # Because the ID didn't exist before, we have recorded all we need to
                continue

            if len(current_positions[key] - self.ID_trajectories[key][prev_time]) > 0:
                self.ID_trajectories[key][t] = current_positions[key] | self.ID_trajectories[key][prev_time]




        # Record attempted activity
        self.attempted.append( [len(self.state.contents[j].vals[0]) for j in range(self.N) ] )

        #print(self.state)

        # Perform the collision, and record deaths
        # Need a function "perform_collision"
        doomed = []
        for j in range(self.N):
            arg1 = self.state.contents[j].vals[0]
            if len(arg1) > 1:
                arg2 = self.state.contents[j].vals[1]
                doomed.append( Package(arg1, arg2) )
                self.state.clear(j)
        self.deaths.append(doomed)

        # Get extinct IDs
        # Need a function "determine_extant"
        currently_alive = set()
        for j in range(self.N):
            currently_alive |= set( self.state.contents[j].vals[0] )

        newly_extinct = self.extant - currently_alive
        self.extinct |= newly_extinct
        self.extant -= self.extinct

        print("Extint at time " + str(t) +": " + str(self.extinct))



        
        # Record actual activity
        self.actual.append( [len(self.state.contents[j].vals[0]) for j in range(self.N) ] )

        # Record the ages of those messages that survive
        # Need a function "record_survivor_ages"
        survivor_ages = []
        for j in range(self.N):
            try:
                survivor_ages.append( len(self.state.contents[j].vals[1][0]) )
            except IndexError:
                survivor_ages.append(0)
        self.ages.append(survivor_ages)


        # Record the IDs present at each node after collision
        # Need a function "record_node_hists"
        next_node_hist = []
        for j in range(self.N):
            try:
                next_node_hist.append( self.state.contents[j].vals[0][0] )
            except IndexError:
                next_node_hist.append(None)
        self.node_hists.append( next_node_hist )


    # Advance the experiment up to the time horizon, self.T. Returns all of the recordings 
    def execute(self):
        for t in range(1, self.T):
            self.advance(t)
        self.executed = True
        return (self.state, self.attempted, self.actual, self.ages, self.deaths)


    ##############################
    ##############################
    # DATA FORMATTING METHODS
    ##############################
    ##############################

    # Age average stuff
    def timewise_average_age(self):
        out = {}
        for t in range(self.T):
            out[t] = sum( self.ages[t] )/self.N
        return out

    def timewise_max_age(self):
        out = {}
        for t in range(self.T):
            out[t] = max(self.ages[t])
        return out


    # Age at death stuff
    def average_death_age(self):
        num_deaths = 0
        age_sum = 0

        for tally in self.deaths:
            for pkg in tally:
                L = len(pkg.vals[0])
                for i in range(L):
                    num_deaths += 1
                    age_sum += len( pkg.vals[1][i] )

        if num_deaths == 0:
            return -1
        return age_sum / num_deaths


    # Death edge stuff
    def timewise_death_edges(self, t):
        out = []
        if t > self.T:
            return out
        
        entry_of_interest = self.deaths[t]

        for package in entry_of_interest:
            M = len(package.vals[1])
            for i in range(M):
                if len(package.vals[1][i]) == 1:
                    out.append( (package.vals[1][i][0], package.vals[1][i][0]) )
                    continue
                out.append( (package.vals[1][i][-2], package.vals[1][i][-1]) )
        return out

    def cumulative_death_edges(self, t0, t1):
        out = {}
        # Loop through range(t0, t1+1)
        for t in range(t0, t1):
            death_edges = self.timewise_death_edges(t)
            for edge in death_edges:
                try:
                    out[edge] += 1
                except KeyError:
                    out[edge] = 1
        return out


    ##############################
    ##############################
    # OUTPUT METHODS
    ##############################
    ##############################

    # Basic outputs
    def write_attempted_csv(self, out_name):
        out_file = open(out_name, "w")

        # Write top line
        st = "Time, "
        for n in range(self.N):
            st += str(n) + ", "
        out_file.write(st[:-2] + "\n")

        # Write the rest of the data
        for t in range(self.T):
            st = str(t) + ", "
            row = self.attempted[t]
            for num in row:
                st += str(num) + ", "
            out_file.write(st[:-2] + "\n")
        out_file.close()
        return None

    def write_actual_csv(self, out_name):
        out_file = open(out_name, "w")

        # Write top column
        st = "Time, "
        for n in range(self.N):
            st += str(n) + ", "
        out_file.write(st[:-2] + "\n")

        # Write the rest of the data
        for t in range(self.T):
            st = str(t) + ", "
            row = self.actual[t]
            for num in row:
                st += str(num) + ", "
            out_file.write(st[:-2] + "\n")
        out_file.close()
        return None

    def write_ages_csv(self, out_name):
        # Get the max age needed
        M = max( set( self.ages[i][j] for i in range(self.T) for j in range(self.N) ) )

        out_file = open(out_name, "w")

        # Write top line
        st = "Time, "
        for age in range(1, M+1):
            st += str(age) + ", "
        out_file.write(st[:-2] + "\n")

        # Write the rest of the data
        for t in range(self.T):
            st = str(t) + ", "
            for age in range(1, M+1):
                st += str( self.ages[t].count(age) ) + ", "
            out_file.write(st[:-2] + "\n")

        out_file.close()
        return None


    def write_timewise_average_age_csv(self, out_name):
        # Get this data
        time_averages = self.timewise_average_age()
        #print(time_averages)

        out_file = open(out_name, "w")

        # Write the top line
        out_file.write("Time, Average Age\n")

        # Write the rest of the data
        for t in range(self.T):
            out_file.write(str(t) + ", " + str(time_averages[t]) + "\n")

        out_file.close()

    def write_timewise_max_age_csv(self, out_name):
        # Get this data
        time_maxes = self.timewise_max_age()

        out_file = open(out_name, "w")

        # Write the top line
        out_file.write("Time, Maximum Age\n")

        # Write the rest of the data
        for t in range(self.T):
            out_file.write( str(t) + ", " + str(time_maxes[t]) + "\n" )

        out_file.close()


    # Death edge outputs
    def write_cumulative_death_edges_csv(self, out_name):
        # First, deep copy the adjacency matrix, and modify it as needed
        mtx = []

        for i in range(self.N):
            row = []
            for j in range(self.N):
                if self.adj[i][j] == 0:
                    row.append(None)
                    continue
                row.append(self.adj[i][j])
            mtx.append(row)

        death_dict = self.cumulative_death_edges(0,self.T)

        death_edges = death_dict.keys()

        for edge in death_edges:
            mtx[edge[0]][edge[1]] = death_dict[edge]

        out_file = open(out_name, "w")

        # Write the first line
        st = ", "
        for i in range(self.N):
            st += str(i) + ", "
        out_file.write(st[:-2] + "\n")

        # Write the remaining lines
        for i in range(self.N):
            st = str(i) + ", "
            for j in range(self.N):
                st += str( mtx[i][j] ) + ", "
            out_file.write(st[:-2] + "\n")

        out_file.close()

        return None


    def write_verif_output_1(self, out_name):
        out_file = open(out_name, "w")

        # Write the first line
        out_file.write( "Time of Death, Message ID, Age at Death, Place of Death, Place Before Death\n" )

        for t in range(self.T):
            tally = self.deaths[t]
            for pkg in tally:
                N = len(pkg.vals[0])
                for i in range(N):
                    msg_id = str( pkg.vals[0][i] )
                    age = str( len( pkg.vals[1][i] ) )
                    place_of_death = str( pkg.vals[1][i][-1] )
                    try:
                        send_to_death = str( pkg.vals[1][i][-2] )
                    except IndexError:
                        send_to_death = str( pkg.vals[1][i][-1] )

                    out_file.write( str(t) + ", " + msg_id + ", " + age + ", " + place_of_death + ", " + send_to_death + "\n" )

        out_file.close()

    def write_verif_output_2(self, out_name):
        out_file = open(out_name, "w")

        # Write the first line
        st = "Time, "
        for i in range(self.N):
            st += str(i) + ", "
        out_file.write(st[:-2] + "\n")

        for t in range(self.T):
            st = str(t) + ", "
            for j in range(self.N):
                st += str( self.node_hists[t][j] ) + ", "
            out_file.write(st[:-2] + "\n")

        out_file.close()



    ##############################
    ##############################
    # THIS CODE IS JUST FOR TRYING OUT NEW IDEAS
    ##############################
    ##############################

    # We need output functions that toss out the transient. So we'll run for 1000 time steps, and then throw out the first 500. This time horizon will
    # be hard coded 

    def avg_age_steady(self, choice=0):
        if self.T <= 500:
            print("Pick a time horizon greater than 500")
            raise AssertionError

        if not self.executed:
            print("Execute first")
            raise AssertionError

        age_sum = 0
        term_count = 0

        for t in range(500, self.T):
            for j in range(self.N):
                age_sum += self.ages[t][j]
                term_count += int(self.ages[t][j] != 0)

        return age_sum / term_count 








