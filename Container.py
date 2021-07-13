import random
from Package import Package

class Container(object):
    def __init__(self, N):
        #self.contents = list(Package([],[]) for _ in range(N))
        self.size = N
        
        self.contents = []
        for i in range(self.size):
            self.contents.append( Package([],[]) )

    def __str__(self):
        st = "{"
        for pkg in self.contents:
            st += str(pkg) + ", "
        st = st[:-2] + "}"
        return st
    
    def fill(self, t, load):
        # Get next batch of tags and injection nodes
        tags = iter( range(t*load, (t+1)*load) )

        injection_nodes = sorted(random.choices(range(self.size), k=load))
        
        # Inject the messages
        for j in injection_nodes:
            self.contents[j].incorporate(Package(tag = [next(tags)], hist = [[j]]))
    
    # Do these methods actually make sense for their intended purposes?
    # Yes, because they are gonna be used in the matrix multiplicaiton
    def clear(self, j):
        self.contents[j].clear()
    
    def record(self, j):
        self.contents[j].record(j)
    
    def incorporate(self, other):
        for j in range(self.size):
            self.contents[j].incorporate(other.contents[j])
    
    def RW_propagate(self, adj):
        #take each message
        #deep copy contents into a buffer array
        buffer = []
        for pkg in self.contents:
            try:
                buffer.append(Package(pkg.vals[0],pkg.vals[1]))
            except IndexError:
                buffer.append(Package([],[]))
        #clear out all old contents to write in new state 
        for i in range(self.size):
            self.contents[i]=Package([],[])
        #take each message
        for pkg in buffer:
            #how many/which outgoing edges go from this message's current node
            destinations = []
        #NEED TO ACCOUNT FOR EMPTY PACKAGES HERE BECAUSE THE ISSUE IS EMPTY PACKAGES.
            if pkg.vals[0] != []:
                for matnav in range(self.size):
                    if adj[pkg.vals[1][0][-1]][matnav] > 0:
                        destinations.append(matnav)
<<<<<<< Updated upstream
            #randomly select a node to go to
            #send the message to that node
                pkg.vals[1][0].append(random.choice(destinations))
        #putting packages into the container in order from the buffer
=======

                # Randomly select a node to go to, and send the message to that node
                if len(destinations)==0:
                    pass
                else:
                    pkg.vals[1][0].append(random.choice(destinations))

        # Put packages into self.contents in order from the buffer
>>>>>>> Stashed changes
        for pkg in buffer:
            if pkg.vals[0] != []:
                j=pkg.vals[1][0][-1]
                self.contents[j].incorporate(pkg) #or make a new package? deep
        return None

    def IS_propagate(self, adj):
        # First, we need a buffer to store the current state
        buffer = []
        for pkg in self.contents:
            try:
                buffer.append(Package(pkg.vals[0], pkg.vals[1]))
            except IndexError:
                buffer.append(Package([],[]))

        # Now, we update the entries in self.contents
        for j in range(self.size):
            self.contents[j].clear()
            for i in range(self.size):
                if adj[i][j] and not buffer[i].is_empty():
                    new_hist = [indiv_hist + [j] for indiv_hist in buffer[i].vals[1]]
                    pkg_to_incorp = Package( buffer[i].vals[0], new_hist)
                    self.contents[j].incorporate(pkg_to_incorp)