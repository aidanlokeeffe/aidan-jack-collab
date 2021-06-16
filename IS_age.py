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

# A Question) Do the ids behave well if we repeatedly incorporate the same message
recorder1 = Package([], [[1]])
recorder2 = Package([], [[2]])
recorders = [recorder1, recorder2]
a = Package([1], [[1]])
id_a = id(a)
for i in range(10):
	a.incorporate( recorders[i%2] )
print("\nWe are testing iterated incorporation")
print(a)
print(id_a == id(a))
print()






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
#random.seed(8)
#ctn = Container(4)
#ctn.fill(0,2)
#print(ctn.contents[0])
#ctn.record(0)
#print(ctn.contents[0])

#incorporate
# 2) Let e denote the empty container. Let a be another container. 
# 2a) Is a.incorporate(e) equal to a element wise? (YES)
# 2b) Is a.incorporate(e) equal to a storage wise? (YES)
random.seed(8)
e = Container(5)
a = Container(5)
a.fill(0,2)
test1 = str(a)
test3 = id(a)
a.incorporate(e)
test2=str(a)
test4 = id(a)
passed = test1 == test2
print('Is a.incorporate(e) equal to a element wise? '+ str(passed))
passed2 = test3 == test4
print('Is a.incorporate(e) equal to a storage wise? '+ str(passed2))


# 3) Let b be another package. 
# 3a) Is e.incorporate(b) equal to b storage wise? (NO)
b = Container(5)
b.fill(0,3)
test1 = id(b)
e.incorporate(b)
test2 = id(e)
passed = test1 == test2
print('Is e.incorporate(b) equal to b storage wise? (NO) '+ str(passed))


# 4) Let c and d be predetermined packages. 
# 4a) Is c.incorporate(d) as expected?
random.seed(8)
c = Container(6)
d=Container(6)
c.fill(0,4)
#print(c)
d.fill(0,4)
#print(d)
c.incorporate(d)
#print(c)
#print('yeet yes fam')

print("\nHere will be the propogation method tests. Good luck!")

# Here is a matrix for testing
'''
entries = [[0,1,0,0,1],
           [1,0,0,1,1],
           [0,1,0,1,0],
           [0,0,1,0,0],
           [1,1,1,1,0]]
'''
N = 3
entries = [[0,1,0],
           [0,0,1],
           [1,0,0]]

test_mat = np.array(entries).reshape((N,N))
print(test_mat)



#RW_propogate
# )) ???
print("\nRandom Walk Test")
print("How it feels to chew 5 Gum: https://www.youtube.com/watch?v=aAzIRaQVbeo")

#IS_propogate
# )) Just work out an example by hand, then run the code
# and see if it works properly

print("\nInformation Spreading Test")

'''
a = Container(N)
random.seed(4)
a.fill(2,2)
print(a)
'''
# Tests
# Does just passing a message around in a loop seem to work?
# In a star topology, do we get the expected result?
# Is it true that nothing happens if we try to propogate an
# empty message, as it should?

N = 3
entries = [[0,1,0],
           [0,0,1],
           [1,0,0]]

test_mat = np.array(entries).reshape((N,N))

a = Container(N)
a.contents[0] = Package([1], [[0]])
print(a)
passed = True

strings = ["{[; []], [1; [0, 1]], [; []]}",
"{[; []], [; []], [1; [0, 1, 2]]}",
"{[1; [0, 1, 2, 0]], [; []], [; []]}",
"{[; []], [1; [0, 1, 2, 0, 1]], [; []]}",
"{[; []], [; []], [1; [0, 1, 2, 0, 1, 2]]}",
"{[1; [0, 1, 2, 0, 1, 2, 0]], [; []], [; []]}"]
count = 0
while passed and count < 6:
	a.IS_propogate(test_mat)
	passed = passed and (str(a) == strings[count])
	count += 1
print("Does IS correctly pass one message in a 3 cycle? " + str(passed))

N = 4
entries = [[0,1,1,1],
           [0,0,0,0],
           [0,0,0,0],
		   [0,0,0,0]]

test_mat = np.array(entries).reshape((N,N))


#star topology test
a = Container(N)
a.contents[0] = Package([1], [[0]])
print(a)
passed = True

strings = ['{[1; [0]], [; []], [; []], [; []]}',
'{[; []], [1; [0, 1]], [1; [0, 2]], [1; [0, 3]]}',
'{[; []], [; []], [; []], [; []]}',
'{[; []], [; []], [; []], [; []]}',
'{[; []], [; []], [; []], [; []]}',
'{[; []], [; []], [; []], [; []]}']
count = 0
while passed and count < 3:
	passed = passed and (str(a) == strings[count])
	a.IS_propogate(test_mat)
	print(a)
	count += 1
print("Does IS correctly pass one message in a 3 cycle? " + str(passed))


























