import numpy as np
import math
from Container import Container
from Package import Package

class Experiment(object):
    # Thought for next time: maybe adj should be a file name, and we
    # read it in like big boys
    def input_matrix(self, inFile):
        matrix = np.genfromtxt(inFile, delimiter = ',')
        if math.isnan(matrix[0][0]):
            matrix = matrix[1:,1:]
        self.adj = matrix
        self.N = len(matrix)
        return None

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
        self.deaths = [] 
        
        if choice==0:
            self.propagate = self.state.RW_propagate
        else:
            self.propagate = self.state.IS_propagate
    '''
    def advance(self, t, debug=False):        
        # Add the new messages
        new_message = Container(self.N)

        print("At start of iteration " + str(t) + ": \n" , self.state)

        new_message.fill(t, self.load)
        print("The new message is: ", new_message)
        
        self.state.incorporate(new_message)
        print("Random injection during iteration " + str(t) + ": \n", self.state)
        
        self.propagate(self.adj)

        print("State before attempts are pruned: ", self.state)

        # Ready to record attempted activity
        self.attempted.append( [len(self.state.contents[j].vals[0]) for j in range(self.N)] )
        
        # The actual collision, with deaths recorded
        doomed = []
        for j in range(self.N):
            arg1 = self.state.contents[j].vals[0]
            if len(arg1) > 1:
                # Seems overkill, but we need to deep copy those who die
                arg2 = self.state.contents[j].vals[1]
                doomed.append( Package(arg1, arg2) )
                self.state.clear(j)
        self.deaths.append(doomed)
        
        self.actual.append([len(self.state.contents[j].vals[0]) for j in range(self.N)])
        #self.ages.append([len(self.state.contents[j].vals[1][0]) for j in range(self.N)])

        survivor_ages = []
        for j in range(self.N):
            try:
                survivor_ages.append( len(self.state.contents[j].vals[1][0] ) )
            except IndexError:
                survivor_ages.append(0)

        #print(survivor_ages)

        print("After deaths for iteration " + str(t) +": \n",self.state,"\n")

        self.ages.append(survivor_ages)
    '''

    def advance(self, t):
        #print("ITERATION " + str(t))
        #print("Last state: " + str(self.state))

        # Propagate the messages according to the chosen rule
        self.propagate(self.adj)
        #print("Propogated: " + str(self.state))

        # Add the random messages after propagating
        new_message = Container(self.N)
        new_message.fill(t, self.load)
        #print("Injection: " + str(new_message))

        self.state.incorporate(new_message)
        #print("Post-injection: " + str(self.state))

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
        #print("Post-deaths: " + str(self.state) + "\n")

        self.actual.append( [len(self.state.contents[j].vals[0]) for j in range(self.N) ] )

        survivor_ages = []
        for j in range(self.N):
            try:
                survivor_ages.append( len(self.state.contents[j].vals[1][0]) )
            except IndexError:
                survivor_ages.append(0)

        self.ages.append(survivor_ages)

    def execute(self):
        for t in range(1, self.T):
            self.advance(t)
        return (self.state, self.attempted, self.actual, self.ages, self.deaths)

    # Output as a csv
    def write_attempted_csv(self, out_name):
        out_file = open(out_name, "w")

        # Write top column
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
        out_file = open(out_name, "w")

        # Write top column
        st = "Time, "
        for n in range(self.N):
            st += "Age at node " + str(n) + ", "
        out_file.write(st[:-2] + "\n")

        # Write the rest of the data
        for t in range(self.T):
            st = str(t) + ", "
            row = self.ages[t]
            for num in row:
                st += str(num) + ", "
            out_file.write(st[:-2] + "\n")
        out_file.close()

        return None


    # This one is kinda hard. To avoid 
    def write_age_at_death_csv(self, out_name):
        return None

    def write_attempted_m(self, out_name):
        return None

    def write_actual_m(self, out_name):
        return None

    def write_ages_m(self, out_name):
        return None

    def write_age_at_death_m(self, out_name):
        return None

textExp = Experiment('testadjmat.csv', 2, 1)