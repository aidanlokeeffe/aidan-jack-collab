import numpy as np
import random
import math
from Package import Package
from Container import Container
from Experiment import Experiment


test_exp = Experiment("testadjmat.csv", 1, 10, choice=1)

T = test_exp.T

test_exp.execute()




for i in range(len(test_exp.deaths)):
	print(str(i) +": " + str(test_exp.deaths[i]))

print()
for i in range(T):
	print(i, test_exp.timewise_death_edges(i))

print()
print(test_exp.cumulative_death_edges(0, T))



test_exp.write_attempted_csv("attempted_test.csv")
test_exp.write_actual_csv("actual_test.csv")
test_exp.write_ages_csv("ages_test.csv")
test_exp.write_cumulative_death_edges_csv("cumulative_death_edges_test.csv")














