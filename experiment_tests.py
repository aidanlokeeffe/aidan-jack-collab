import numpy as np
import random
import math
from Package import Package
from Container import Container
from Experiment import Experiment


test_exp = Experiment("testadjmat.csv", 2, 10, choice=1)

T = test_exp.T


#print("THESE ARE THE STATES OVER TIME, BEFORE COLLISION")
test_exp.execute()

print()
test_dict = test_exp.ID_trajectories
keys = test_dict.keys()
for key in keys:
	print(str(key) + ": " + str(test_dict[key]))






#print()
#for i in range(len(test_exp.deaths)):
	#print(str(i) +": " + str(test_exp.deaths[i]))

#print()
#for i in range(T):
	#print(i, test_exp.timewise_death_edges(i))

#print()
#print(test_exp.cumulative_death_edges(0, T))

'''
print()
print("HERE ARE DEATHS")
for t in range(T):
	print("t = " + str(t) +": " + str(test_exp.deaths[t]))



test_exp.write_attempted_csv("attempted_test.csv")
test_exp.write_actual_csv("actual_test.csv")
test_exp.write_ages_csv("ages_test.csv")
test_exp.write_cumulative_death_edges_csv("cumulative_death_edges_test.csv")
test_exp.write_timewise_average_age_csv("timewise_average_age_test.csv")
test_exp.write_timewise_max_age_csv("timewise_max_age_test.csv")
test_exp.write_verif_output_1("verif_1.csv")
test_exp.write_verif_output_2("verif_2.csv")


print("\nLOOK HERE")
i = 0
while True:
	try:
		print(str(test_exp.ages[i]) + ": " + str( sum(test_exp.ages[i]) / 5 )   )
		i+=1
	except IndexError:
		break
print()

print("AVERAGE AGE AT DEATH")
print( test_exp.average_death_age() )

print()
print("NODE HISTS")
print(test_exp.node_hists)
'''

















