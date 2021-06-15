class Package(object):
    def __init__(self, tag, hist):
        self.vals = [tag, hist]
    
    # Okay, so when we do the loop for matrix multiplication, we will need a method that computes the combination of 
    # however many packages we have
    def incorporate(self, other):
        self.vals[0] += other.vals[0]
        self.vals[1] += other.vals[1]
        return None
    
    # We might now even need this method, but we'll hold onto it until we have proof that we don't
    def clear(self):
        self.vals = [list(),list()]
        return None
    

    # (!!!) We might not even need this function
    def record(self, j):
        # The empty package should not have a record
        if len(self.vals[0])==0:
            return None
        self.vals[1][0] += [j]
        return None
        #cannot record when initializing because it will double the history of the first node. Only record when package moves
    
    def __str__(self):
        st = "["
        
        if len(self.vals[0]) == 0:
            return "[; []]"
        
        for _ in range(len(self.vals[0])):
            st += str(self.vals[0][_])+","
        st = st[:-1] + "; "
        for _ in range(len(self.vals[1])):
            st += str(self.vals[1][_])+","
        st = st[:-1]+"]"
        return(st)
    
    def __repr__(self):
        return str(self)

