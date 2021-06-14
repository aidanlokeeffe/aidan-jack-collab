import numpy as np
import random
from Package import Package
from Container import Container
from Experiment import Experiment

#######################
# PACKAGE TESTS
#######################

# __init__
# 1) Is the empty package what it's supposed to be?
a = Package()
passed = len(a.vals[0])==0 and len(a.vals[1])==0
print("TEST: Is the empty package actually empty? " + str(passed))

# 1.5) Initialize a non empty package of your choosing. 
b = Package([1], [[1,2]])
# 1.5a) Is is element wise equal to what it should be?
passed = (b.vals[0] == [1]) and (b.vals[1] == [[1,2]])
print("TEST: Does package initialization seem to work? " + str(passed))



# incorporate
# 2) Let e denote the empty package. Let a be another package. 
# 2a) Is a.incorporate(e) equal to a element wise? (YES)
# 2b) Is a.incorporate(e) equal to a storage wise? (YES)

# 3) Let b be another package. 
# 3a) Is e.incorporate(b) equal to b storage wise? (NO)

# 4) Let c and d be predetermined packages. 
# 4a) Is c.incorporate(d) as expected?

# clear 
# 5) Make a new nonempty package. Clear it. Is it clear?

# record
# 6) Make a nonempty package. Tell it to record, say, 6. 
# 6a) Did it record 6?

# __str__
# 7) Print the empty package. Is the representation correct?

# 8) Print a nonempty package. Is the representation correct?

# __repr__
# 9) Repeat 7 but with __repr__

# 10) Repeat 8 but with __repr__

#######################
# CONTAINER TESTS
#######################


#__init__
# 11) Create a package of size 5, say. Are all of its components
# empty?

#fill
# ???

#clear
# 14) Create a Container. Fill it. Clear it. Did it work?

#record
# 15) Create a Container. Fill it. Print the first component.
# record some value, say 3. Print the first component again. 
# Did it work?

#incorporate
# 2) Let e denote the empty package. Let a be another package. 
# 2a) Is a.incorporate(e) equal to a element wise? (YES)
# 2b) Is a.incorporate(e) equal to a storage wise? (YES)

# 3) Let b be another package. 
# 3a) Is e.incorporate(b) equal to b storage wise? (NO)

# 4) Let c and d be predetermined packages. 
# 4a) Is c.incorporate(d) as expected?

#RW_propogate
# )) ???

#IS_propogate
# )) Just work out an example by hand, then run the code
# and see if it works properly



























'''
import numpy as np
import random
from Package import Package
from Pitstop import Pitstop
>>>>>>> 27f8957b49dec2888f1d73ab5f565c6e6b470a56

# Components of special pitstops
def z1(x):
	return 0
def z2(x):
	return []
def z3(x):
	return []

def o1(x):
	return x
def o2(x):
	return x
def make_o3j(j):
	def o3(x):
		try:
			return [ x[0] + [j] ]
		except IndexError:
			return [[j]]
	return o3

# Special pitstops themselves
zero = Pitstop(z1,z2,z3)
def one_j(j):
	return Pitstop(o1, o2, make_o3j(j))

# Array multiplication function
def array_mult(pkg_arr, pit_arr):
	N = pkg_arr.shape[0] 
	assert(N == pit_arr.shape[0])

	out = []
	for j in range(N):
		component = zero
		for i in range(N):
			component = component + pit_arr[i,j].apply(pkg_arr[i])
		out.append(component)
	return out

def make_xi(N):
	nodes = list(range(N))

def xi(N, tag):
	j = random.sample( list(range(N)))



def make_samp(N,L):
        randys = random.sample(list(range(N)), L)
        def samp():
                sampy = []
                for _ in range(L):
                        sampy.append(Package(1, t*L+_, [[randys[_]]]))
                return sampy
        return samp()





# Read the connectome data
# For now, we'll just have a dummy matrix
adj = np.array([[0,0,0,0,0,0,1],
 				[0,0,0,1,0,0,0],
 				[1,0,0,0,1,0,0],
 				[0,0,1,0,0,0,0],
 				[1,1,0,0,0,1,0],
 				[1,1,0,0,0,1,0],
 				[0,1,1,0,0,0,0],
 				[1,0,0,1,0,0,0]])

# We will be able to get N when we read the file. For now, it will be hard coded
N = 7

pits = []
for i in range(7):
	row = []
	for j in range(7):
		if adj[i,j]:
			pits.append(one_j(j))
			continue
		pits.append(zero)






# Replace all the elements with pitstops

# Randomly generate packages 
'''