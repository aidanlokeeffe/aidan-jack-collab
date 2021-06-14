class Experiment(object):
    # Thought for next time: maybe adj should be a file name, and we
    # read it in like big boys
    def __init__(self, adj, load, T, choice=0):
        # Inputs
        self.adj = adj
        self.load = load
        self.T = T
        self.N = len(adj)
        
        # Initialize dynamical variable
        self.state = Containter(self.N).fill(0, self.load)
        
        # Results
        self.attempted = []
        self.actual = []
        self.ages = []
        self.deaths = []
        
        # NOTE: THESE WILL BE UPDATED INSIDE OF THE FUNCTION COLLIDER, EXCEPT FOR AT TIME 0
        # This will always work for attempted
        self.attempted.append( [len(self.state[j][0]) for j in range(self.N)] )
        # We need to apply collision first for this to work
        self.actual.append([len(self.state[j][0]) for j in range(self.N)]) 
        # This should also be computed only after collision
        self.ages.append([len(self.state[j][1]) for j in range(self.N)])
        # This will be an array of arrays of dead packages, with one inner array per timestep            
        self.deaths = [] 
        
        if choice==0:
            self.propogate = self.state.RW_propogate
        else:
            self.propogate = self.state.IS_propogate
    
    def advance(self, t):        
        # Propogate
        self.state.propogate(self.adj)
        
        # Add the new messages
        self.state.incorporate( Containter(self.N).fill(t, self.load) )
        
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