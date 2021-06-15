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
        for j in range(self.N):
            self.contents[j].incorporate(other.contents[j])
    
    def RW_propogate(self, adj):
        #take each message
        #deep copy contents into a buffer array
        buffer = []
        for pkg in self.contents:
            try:
                buffer.append(Package(pkg[0],pkg[1]))
            except IndexError:
                buffer.append(Package([],[]))
        #clear out all old contents to write in new state 
        for i in range(self.size):
            self.contents[i]=Package([],[])
        #take each message
        for pkg in buffer:
            #how many/which outgoing edges go from this message's current node
            destinations = []
            for matnav in range(self.size):
                if adj[pkg.vals[1][0][-1]][matnav] > 0:
                    destinations.append(matnav)
            #randomly select a node to go to
            #send the message to that node
            pkg.vals[1][0].append(random.choice(destinations))
        #putting packages into the container in order from the buffer
        for pkg in buffer:
            j=pkg.vals[1][0][-1]
            self.contents[j].incorporate(pkg) #or make a new package? deep
        return None
    
    def IS_propogate(self, adj):
        buffer = []
        for pkg in self.contents:

            try:
                buffer.append( Package(pkg.vals[0], pkg.vals[1]) )
            except IndexError:
                buffer.append( Package([],[]) )
        
        # Propogate messages 
        for i in range(self.size):
            self.clear(i)
            for j in range(N):
                if adj[i][j]:
                    self.contents[i].incorporate(buffer[j])
#age is history length - 1