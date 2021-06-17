import numpy as np
import random
import math
from Package import Package
from Container import Container
from Experiment import Experiment

test_exp = Experiment("testadjmat.csv", 1, 2, choice=1)

# Does the experiment have all the needed attributes?
print(test_exp.load)
print(test_exp.T)
print(test_exp.adj)
print(test_exp.N)
print(test_exp.choice)
print(test_exp.propagate,"\n")
# Yes, it does.
# This also tests input_matrix

# Testing advance


# Print before
print("State at time 0")
print(test_exp.attempted)
print(test_exp.actual)
print(test_exp.ages)
print(test_exp.deaths)


random.seed(4)
test_exp.advance(1)

print("\nState at time 1")
print(test_exp.attempted)
print(test_exp.actual)
print(test_exp.ages)
print(test_exp.deaths)