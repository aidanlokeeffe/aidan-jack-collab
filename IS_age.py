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
a = Package([],[])
passed = len(a.vals[0])==0 and len(a.vals[1])==0
print("TEST: Is the empty package actually empty? " + str(passed))

# 1.5) Initialize a non empty package of your choosing. 
b = Package([1], [[1,2]])
# 1.5a) Is is element wise equal to what it should be?
passed = (b.vals[0] == [1]) and (b.vals[1] == [[1,2]])
print("TEST: Does package initialization seem to work? " + str(passed))



# incorporate
# 2) Let e denote the empty package. Let a be another package. 
e=Package([],[])
a=Package([1],[[1,2,3]])
# 2a) Is a.incorporate(e) equal to a element wise? (YES)
a.incorporate(e)
passed = a.vals[0]==[1]
passed2 = a.vals[1]==[[1,2,3]]
print('Is a.incorporate(e) equal to a element wise? ' + str(passed) + str(passed2))
# 2b) Is a.incorporate(e) equal to a memory wise? (YES)
e=Package([],[])
a=Package([1],[[1,2,3]])
id_a = id(a)
a.incorporate(e)
passed = id_a == id(a)
print('Is a.incorporate(e) equal to a memory wise?' + str(passed))

# 3) Let b be another package. 
b=Package([43821], [[1,2,3,5,8,13]])
e=Package([],[])
# 3a) Is e.incorporate(b) equal to b memory wise? (NO)
id_e = id(e)
e.incorporate(b)
passed = id_e == id(b)
print('Is e.incorporate(b) equal to b memory wise? (NO)' + str(passed))

# 4) Let c and d be predetermined packages. 
c=Package([42069],[[420,69,23489214]])
d=Package([127],[[2,4,6,8]])
# 4a) Is c.incorporate(d) as expected?
c.incorporate(d)
passed = c.vals[0] == [42069,127]
passed2 = c.vals[1] == [[420,69,23489214],[2,4,6,8]]
print(' Is c.incorporate(d) as expected? ' +str(passed)+str(passed2))
# clear 
# 5) Make a new nonempty package. Clear it. Is it clear?
packagey = Package([420],[[6,9]])
packagey.clear()
passed = len(packagey.vals[0])==0
passed2 = len(packagey.vals[1])==0
print('Make a new nonempty package. Clear it. Is it clear? ' + str(passed)+str(passed2))

# record
# 6) Make a nonempty package. Tell it to record, say, 6. 
# 6a) Did it record 6?
pack = Package([5],[[0,1,2,3,4,5]])
pack.record(6)
passed = pack.vals[1][0][-1]==6
print('Did record record 6? ' + str(passed))

# __str__
# 7) Print the empty package. Is the representation correct?
obama = Package([],[])
fullpacky = Package([420],[[69]])
passed = str(obama) == "[; []]"
print('Print the empty package. Is the representation correct? ' + str(passed))
# 8) Print a nonempty package. Is the representation correct?
passed = str(fullpacky) == "[420; [69]]"
print('Print a nonempty package. Is the representation correct? '+ str(passed))

# __repr__
# 9) Repeat 7 but with __repr__
obama = Package([],[])
fullpacky = Package([420],[[69]])
passed = repr(obama) == "[; []]"
print('Print the empty package. Is the representation correct? ' + str(passed))

# 10) Repeat 8 but with __repr__
passed = repr(fullpacky) == "[420; [69]]"
print('Print a nonempty package. Is the representation correct? '+ str(passed))

#######################
# CONTAINER TESTS
#######################


#__init__
# 11) Create a container of size 5, say. Are all of its components
# empty?
# FOCK

'''
cont = Container(5)

booly = True
while booly:
	for i in range(5):
		for j in range(2):
			booly = cont.contents[i][j].isempty() and booly
print('Create a container of size 5, say. Are all of its components empty? '+ str(booly))
'''

ctn = Container(5)

passed = True
for i in range(5):
	passed = passed and (ctn.contents[i].vals[0] == [])
	passed = passed and (ctn.contents[i].vals[1] == [])
	if not passed:
		break
print("Does container initialization work? " + str(passed))
	

#fill
random.seed(123456789)
ctn = Container(6)
ctn.fill(0, 3)
passed = str(ctn) == "{[; []], [; []], [; []], [0,1; [3],[3]], [; []], [2; [5]]}"
print("Does filling work as preditcted? " + str(passed))

#clear
# 14) Create a Container. Fill it. Clear it. Did it work?
ctn.clear(3)
passed = str(ctn) == "{[; []], [; []], [; []], [; []], [; []], [2; [5]]}"
print("Create a Container. Fill it. Clear it. Did it work? " + str(passed))

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