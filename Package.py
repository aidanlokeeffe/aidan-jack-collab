class Package(object):
    def __init__(self, tag = [], hist = []):
        self.vals = [tag, hist]
    
    # Okay, so when we do the loop for matrix multiplication, we will need a method that computes the combination of 
    # however many packages we have
    def incorporate(self, other):
        self.vals[0] += other.vals[0]
        self.vals[1] += other.vals[1]
        return None
    
    # We might now even need this method, but we'll hold onto it until we have proof that we don't
    def clear(self):
        self.vals = [[],[]]
        return None
    
    def record(self, j):
        # The empty package should not have a record
        if len(self.vals[0]==0):
            return None
        self.vals[1][0].append(j)
        return None
    
    def __str__(self):
        st = "["
        
        if self.vals[0] == []:
            return "[[]; []]"
        
        for _ in range(len(self.vals[0])):
            st += str(self.vals[0][_])+","
        st = st[:-1] + "; "
        for _ in range(len(self.vals[1])):
            st += str(self.vals[1][_])+","
        st = st[:-1]+"]"
        return(st)
    
    def __repr__(self):
        return str(self)


'''
class Package(object):
	# val: int; tag: array of int; hist; 2D array, the inner arrays will contain integers
	# default is the empty package
	def __init__(self, n=0, tag=[], hist=[]):
		self.val = [n, tag, hist]

	def __add__(self, other):
		args = (self.val[_] + other.val[_] for _ in range(2))
		return Package(*args)

	def n(self):
		return self.val[0]

	def tag(self):
		return self.val[1]

	def hist(self):
		return self.val[2]
'''