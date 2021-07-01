'''
This is the package class. A package is an array of two components. The first 
component is called the ID, although since id is a reserved word in Python, we 
call it the tag instead. The second component is called the history. The two
components are stored in the attribute called vals.

Now, what actually are each component? This might be a little confusing at 
first, but when we get to incorporation, it will make sense.

The ID component is a 1-D array. It can contain any number of integers, 
including 0 integers. 

The history component is either empty, or it is a 2-D array containing 
the track record for the respective ID.

The first kind of package is the empty package. Its ID is [], and its
history is [] too. Its string representation is 

"[; []]"

We will call a package "regular" if its ID is length 1, and its history is 
length 1 too (note that history being length 1 means that there is onle one
inner array in the history). An example is a package with ID [23], and history
[1,2,3,4,7,4,6,1,34]. Its string representation is 

"[23; [1,2,3,4,7,4,6,1,34]]"

Finally, we have "irregular" packages, which have IDs and histories of length
greater than 1. An example is a package with string representation

"[1,2; [1,2,3],[4,3]]"

Okay, you may be wondering: why do irregular packages exist? First, let N be
the number of nodes in a network. Irregular packages then allow two messages to
occupy the same node while still being able to represent all of the messages in
the network with an array of length N. Such an array is called a container, and 
further discussion can be found in that class file. This allows us to use the 
adjacency matrix to pass messages around, while also recording their IDs and 
histories.

Now, we discuss incorporation. Bear in mind that the primary purpose of 
Packages is to replace scalars, so that we can think of IS as right 
multiplication by the adjacency matrix. This means that we need a way to add 
Packages. Incorporation is the addition.


The function incorporate appends the ID and history of another message onto 
those of the self. This was done so that the address of self can be used to 
store the output package, instead of allocating new memory every time two 
packages are combined, which causes slowdown.

The record function takes the place of multiplication by 1. We have to append
the index of a node into the history, but the ID is preserved.

Finally, the clear function takes the place of multiplication by 0.
'''


class Package(object):
    # Constructor
    def __init__(self, tag, hist):
        self.vals = [tag, hist]
    
    # Combines two packages into one
    def incorporate(self, other):
        self.vals[0] += other.vals[0]
        self.vals[1] += other.vals[1]
        return None
    
    # Turns self into the empty package
    def clear(self):
        self.vals = [list(),list()]
        return None
    
    # Tells if self is empty
    def is_empty(self):
        return (len(self.vals[0]) == 0) and (len(self.vals[1]) == 0)


    # Records the value j to self's history
    def record(self, j):
        # The empty package should not have a record
        if len(self.vals[0])==0:
            return None
        self.vals[1][0] += [j]
        return None

    # String representation    
    def __str__(self):
        st = "["
        
        # Check if what we are printing is the empty package
        if len(self.vals[0]) == 0:
            return "[; []]"
        
        # Write all the IDs
        for _ in range(len(self.vals[0])):
            st += str(self.vals[0][_])+","

        # Write the semicolor separating IDs from histories
        st = st[:-1] + "; "

        # Write each history
        for _ in range(len(self.vals[1])):
            st += str(self.vals[1][_])+","
        st = st[:-1]+"]"

        return st
    
    # Representation for printing in lists
    def __repr__(self):
        return str(self)

