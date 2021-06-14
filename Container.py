import random
class Containter(object):
    def __init__(self, N):
        self.contents = list(Package() for _ in range(N))
        self.size = N
    
    def fill(self, t, load):
        # Get next batch of tags and injection nodes
        tags = iter( range(t*load, (t+1)*load) )
        injection_nodes = sorted(random.choices(self.size, load))
        
        # Inject the messages
        for j in injection_nodes:
            self.contents[j].combine(Package(tag = [next(tags)], hist = [[j]]))
    
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
        for pkg in self.contents:
            #how many/which outgoing edges go from this message's current node
            destinations = []
            for matnav in range(self.size):
                if adj[pkg.vals[1][0][-1]][matnav] > 0:
                    destinations.append(matnav)
            #randomly select a node to go to
            #send the message to that node
            pkg.vals[1][0].append(random.choice(destinations))
        return None
    
    def IS_propogate(self, adj):
        buffer = []
        for pkg in self.contents:
            buffer.append(pkg)
        
        # I have a feeling this will be buggy
        for i in range(self.size):
            self.clear(i)
            for j in range(N):
                if adj[i][j]:
                    self.contents[i].incorporate(buffer[j])

#age is history length - 1
            
    
