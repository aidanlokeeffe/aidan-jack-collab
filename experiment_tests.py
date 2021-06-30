import numpy as np
import random
import math
from Package import Package
from Container import Container
from Experiment import Experiment
import Barchart_animator
import threed_plotter 


nodes = 91
prob = .2

matrix = []
count = 0
for i in range(nodes):
	L=[0]*nodes
	for j in range(nodes):
		if j!=i:
			randy=random.random()
			if randy<prob:
				L[j]=1
				count+=1
	matrix.append(L)
np.savetxt("testadjmat.csv", matrix, delimiter=',')


test_exp = Experiment("testadjmat.csv", 9, 10000, choice=0)

T = test_exp.T

test_exp.execute()

#print()
#for i in range(len(test_exp.deaths)):
	#print(str(i) +": " + str(test_exp.deaths[i]))

#print()
#for i in range(T):
	#print(i, test_exp.timewise_death_edges(i))

#print()
#print(test_exp.cumulative_death_edges(0, T))



test_exp.write_attempted_csv("attempted_test.csv")
test_exp.write_actual_csv("actual_test.csv")
test_exp.write_ages_csv("ages_test.csv")
test_exp.write_cumulative_death_edges_csv("cumulative_death_edges_test.csv")
#test_exp.write_nodewise_average_age_csv("nodewise_average_age_test.csv")
#test_exp.write_timewise_average_age_csv("timewise_average_age_test.csv")


print("\nLOOK HERE")
i = 0
avgs = []
while True:
	try:
		avgmaker = test_exp.ages[i]
		avgmaker = list(filter(lambda a: (a > 0), avgmaker))
		avgy = sum(avgmaker)/len(avgmaker)
		print(str(test_exp.ages[i]) + ": " + str(avgy))
		avgs.append(avgy)
		i+=1
	except IndexError:
		break
avgs = avgs[1000:]
trueavg = sum(avgs)/len(avgs)
print("THE AVERAGE MESSAGE AGE WAS " + str(trueavg))


Barchart_animator.animateBarchart('attempted_test.csv')
Barchart_animator.animateBarchart('actual_test.csv')
Barchart_animator.animateBarchart('ages_test.csv')
threed_plotter.plotKillingEdge('cumulative_death_edges_test.csv')



test_exp = Experiment("monkey1unweight.csv", 9, 10000, choice=0)

T = test_exp.T

test_exp.execute()

#print()
#for i in range(len(test_exp.deaths)):
	#print(str(i) +": " + str(test_exp.deaths[i]))

#print()
#for i in range(T):
	#print(i, test_exp.timewise_death_edges(i))

#print()
#print(test_exp.cumulative_death_edges(0, T))



test_exp.write_attempted_csv("attempted_test.csv")
test_exp.write_actual_csv("actual_test.csv")
test_exp.write_ages_csv("ages_test.csv")
test_exp.write_cumulative_death_edges_csv("cumulative_death_edges_test.csv")
#test_exp.write_nodewise_average_age_csv("nodewise_average_age_test.csv")
#test_exp.write_timewise_average_age_csv("timewise_average_age_test.csv")


print("\nLOOK HERE")
i = 0
avgs = []
while True:
	try:
		avgmaker = test_exp.ages[i]
		avgmaker = list(filter(lambda a: (a > 0), avgmaker))
		avgy = sum(avgmaker)/len(avgmaker)
		print(str(test_exp.ages[i]) + ": " + str(avgy))
		avgs.append(avgy)
		i+=1
	except IndexError:
		break
avgs = avgs[1000:]
trueavg = sum(avgs)/len(avgs)
print("THE AVERAGE MESSAGE AGE WAS " + str(trueavg))


Barchart_animator.animateBarchart('attempted_test.csv')
Barchart_animator.animateBarchart('actual_test.csv')
Barchart_animator.animateBarchart('ages_test.csv')
threed_plotter.plotKillingEdge('cumulative_death_edges_test.csv')



print(count)