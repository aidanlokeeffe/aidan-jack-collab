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

# 1.5) Initialize a non empty package of your choosing. 
# 1.5a) Is is element wise equal to what it should be?


# incorporate
# 2) Let e denote the empty package. Let a be another package. 
# 2a) Is a.incorporate(e) equal to a element wise? (YES)
# 2b) Is a.incorporate(e) equal to a storage wise? (YES)

# 3) Let b be another package. 
# 3a) Is e.incorporate(b) equal to b storage wise? (NO)

# 4) Let c and d be predetermined packages. 
# 4a) Is c.incorporate(d) as expected?

# 5) 

































'''
import numpy as np
import random
from Package import Package
from Pitstop import Pitstop

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