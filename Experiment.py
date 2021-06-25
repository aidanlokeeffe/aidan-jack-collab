import numpy as np
import math
from Container import Container
from Package import Package

class Experiment(object):
    ##############################
    # SETUP METHODS
    ##############################
    def __init__(self, fileName, load, T, choice=0):
        # Inputs
        self.load = load
        self.T = T
        self.input_matrix(fileName)
        self.choice = choice

        
        # Initialize dynamical variable
        self.state = Container(self.N)
        self.state.fill(0, self.load)
        
        # Results
        self.attempted = []
        self.actual = []
        self.ages = []
        self.deaths = []
        
        # NOTE: THESE WILL BE UPDATED INSIDE OF THE FUNCTION COLLIDER, EXCEPT FOR AT TIME 0
        # This will always work for attempted
        self.attempted.append( [len(self.state.contents[j].vals[0]) for j in range(self.N)] )
        # We need to apply collision first for this to work
        self.actual.append([len(self.state.contents[j].vals[0]) for j in range(self.N)]) 
        # This should also be computed only after collision
        self.ages.append([len(self.state.contents[j].vals[1]) for j in range(self.N)])
        # This will be an array of arrays of dead packages, with one inner array per timestep            
        self.deaths.append([]) 
        
        if choice==0:
            self.propagate = self.state.RW_propagate
        else:
            self.propagate = self.state.IS_propagate


    def input_matrix(self, inFile):
        matrix = np.genfromtxt(inFile, delimiter = ',')
        if math.isnan(matrix[0][0]):
            matrix = matrix[1:,1:]
        self.adj = matrix
        self.N = len(matrix)
        return None


    ##############################
    # DYNAMIC METHODS
    ##############################
    def advance(self, t):
        # Propagate the messages according to the chosen rule
        self.propagate(self.adj)
        
        # Add the random messages after propagating
        new_message = Container(self.N)
        new_message.fill(t, self.load)
        
        self.state.incorporate(new_message)
        
        # Record everything as needed
        self.attempted.append( [len(self.state.contents[j].vals[0]) for j in range(self.N) ] )

        # Perform the collision, and record deaths
        doomed = []
        for j in range(self.N):
            arg1 = self.state.contents[j].vals[0]
            if len(arg1) > 1:
                arg2 = self.state.contents[j].vals[1]
                doomed.append( Package(arg1, arg2) )
                self.state.clear(j)
        self.deaths.append(doomed)
        
        self.actual.append( [len(self.state.contents[j].vals[0]) for j in range(self.N) ] )

        survivor_ages = []
        for j in range(self.N):
            try:
                survivor_ages.append( len(self.state.contents[j].vals[1][0]) )
            except IndexError:
                survivor_ages.append(0)

        self.ages.append(survivor_ages)

    def execute(self):
        print("HERE ARE THE STATES")
        print( "t = 0: " + str(self.state) )
        for t in range(1, self.T):
            self.advance(t)
            print( "t = " + str(t) + ": " + str(self.state) ) 
        return (self.state, self.attempted, self.actual, self.ages, self.deaths)

    ##############################
    # DATA METHODS
    ##############################
    # Average age stuff
    '''
    def nodewise_average_age(self):
        out = {}
        for j in range(self.N):
            entry = 0
            for t in range( self.T ):
                entry += self.ages[t][j]
            out[j] = (entry / self.T)
        return out
    '''

    def timewise_average_age(self):
        out = {}
        for t in range(self.T):
            out[t] = sum( self.ages[t] )/self.N
        return out




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
    # OUTPUT METHODS
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



    # Average age outputs
    '''
    def write_nodewise_average_age_csv(self, out_name):
        # Get this data
        node_averages = self.nodewise_average_age()

        out_file = open(out_name, "w")

        # Write the top line
        out_file.write("Node, Average Age\n")

        # Write the rest of the data
        for j in range(self.N):
            out_file.write(str(j) + ", " + str(node_averages[j]) + "\n")

        out_file.close()
    '''

    def write_timewise_average_age_csv(self, out_name):
        # Get this data
        time_averages = self.timewise_average_age()
        print(time_averages)

        out_file = open(out_name, "w")

        # Write the top line
        out_file.write("Time, Average Age\n")

        # Write the rest of the data
        for t in range(self.T):
            out_file.write(str(t) + ", " + str(time_averages[t]) + "\n")

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

