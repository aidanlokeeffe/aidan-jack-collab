import numpy as np
import math
from Container import Container
from Package import Package

class Experiment(object):
    # Thought for next time: maybe adj should be a file name, and we
    # read it in like big boys
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
    
    def input_matrix(self, inFile):
        matrix = np.genfromtxt(inFile, delimiter = ',')
        if math.isnan(matrix[0][0]):
            matrix = matrix[1:,1:]
        self.adj = matrix
        self.N = len(matrix)
        return None

    def advance(self, t):        
        if self.choice==0:
            self.state.RW_propagate(self.adj)
        else:
            self.state.IS_propagate(self.adj)
        
        # Add the new messages
        self.state.incorporate( Container(self.N).fill(t, self.load) )
        
        # Ready to record attempted activity
        self.attempted.append( [len(self.state[j][0]) for j in range(self.N)] )
        
        # The actual collision, with deaths recorded
        doomed = []
        for j in range(self.N):
            if len(self.state[j][0]) > 1:
                # Seems overkill, but we need to deep copy those who die
                doomed.append(Package( self.state[0], self.state[1] ))
                self.state.clear(j)
        self.deaths.append(doomed)
        
        self.actual.append([len(self.state[j][0]) for j in range(self.N)])
        self.ages.append([len(self.state[j][1]) for j in range(self.N)])
    
    
    
    def execute(self):
        for t in range(1, self.T):
            self.advance(t)
        return (self.state, self.attempted, self.actual, self.ages, self.deaths)

    def read_adj(self, in_file):
        return None

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
            row = self.actual[t]
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