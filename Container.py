'''
This class depends on the Package class, so please read the comments on that 
class file if this code is confusing.

A container is a length N array of packages. The j-th component of a container
represents the message at node j. If the j-th component is the empty package, 
then no message is at node j.

The fill function takes paramaters t and load. t is the current timestep, and
ties into the experiment class. load is the number of messages to be injected.
The reason we need the time is so we can generate load unique message IDs.
Both random walk and information spreading require a random injection of
messages, hence the need to import random here.

clear, record, and incorporate are extension of the corresponding function from
the Package class

The function IS_propagate takes an adjacency matrix, and sends each message 
down every outgoing edge from its current position, recording as needed. 
RW_propagate does a similar thing, but with an unbiased random walk instead.
Note that these methods do not account for collisions; that happens in the 
experiment class.
'''


import random
from Package import Package

class Container(object):
    # Constructor
    def __init__(self, N):
        self.size = N
        
        self.contents = []
        for i in range(self.size):
            self.contents.append( Package([],[]) )

    # String representation
    def __str__(self):
        st = "{"
        for pkg in self.contents:
            st += str(pkg) + ", "
        st = st[:-2] + "}"
        return st
    
    # Fill self with random contents
    def fill(self, t, load):
        # Get next batch of IDs
        tags = iter( range(t*load, (t+1)*load) )

        # Get next batch of injection nodes
        injection_nodes = sorted(random.choices(range(self.size), k=load))
        
        # Inject the messages
        for j in injection_nodes:
            self.contents[j].incorporate(Package(tag = [next(tags)], hist = [[j]]))
    
    # Turn the j-th component into the empty package
    def clear(self, j):
        self.contents[j].clear()
    
    # Record j into the j-th component's history
    def record(self, j):
        self.contents[j].record(j)
    
    # Incorpoprate another package into self component wise
    def incorporate(self, other):
        for j in range(self.size):
            self.contents[j].incorporate(other.contents[j])
    
    
    # Unbiased random walks
    def RW_propagate(self, adj):
        # Deep copy the current contents to a buffer
        buffer = []
        for pkg in self.contents:
            try:
                buffer.append(Package(pkg.vals[0],pkg.vals[1]))
            except IndexError:
                buffer.append(Package([],[]))

        # Clear out the old contents
        for i in range(self.size):
            self.contents[i]=Package([],[])
        
        for pkg in buffer:
            # Get the possible destinations, and only proceed if the old package was not empty
            destinations = []
            if pkg.vals[0] != []:
                for matnav in range(self.size):
                    if adj[pkg.vals[1][0][-1]][matnav] > 0:
                        destinations.append(matnav)

                # Randomly select a node to go to, and send the message to that node
                if len(destinations) != 0:
                    pkg.vals[1][0].append(random.choice(destinations))

        # Put packages into self.contents in order from the buffer
        for pkg in buffer:
            if pkg.vals[0] != []:
                j=pkg.vals[1][0][-1]
                self.contents[j].incorporate(pkg) #or make a new package? deep
        return None


    # Information spreading
    def IS_propagate(self, adj):
        # Deep copy the current contents to a buffer
        buffer = []
        for pkg in self.contents:
            try:
                buffer.append(Package(pkg.vals[0], pkg.vals[1]))
            except IndexError:
                buffer.append(Package([],[]))

        # Now update the comments
        for j in range(self.size):
            self.contents[j].clear()
            for i in range(self.size):
                # Check if there is an edge and the i-th component of the old contents is not empty
                if adj[i][j] and not buffer[i].is_empty():
                    # Get the updated history of this package
                    new_hist = [indiv_hist + [j] for indiv_hist in buffer[i].vals[1]]
                    
                    # Make the new component
                    pkg_to_incorp = Package( buffer[i].vals[0], new_hist)

                    # Incorporate
                    self.contents[j].incorporate(pkg_to_incorp)