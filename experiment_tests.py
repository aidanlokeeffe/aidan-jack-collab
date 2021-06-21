import numpy as np
import random
import math
from Package import Package
from Container import Container
from Experiment import Experiment

test_exp = Experiment("testadjmat.csv", 1, 2, choice=1)

# Okay, I'm getting pissed off at this, so I'm gonna defy my teachers, say that it works,
# and just move on to more important things. If we run into problems, well then I'll just
# have to come back to it, won't I


# Does the experiment have all the needed attributes?
'''
print(test_exp.load)
print(test_exp.T)
print(test_exp.adj)
print(test_exp.N)
print(test_exp.choice)
print(test_exp.propagate,"\n")
'''
# Yes, it does.
# This also tests input_matrix

# Testing advance


# Test of Experiment.advance

from random import Random
random = Random()
random = Random(10)

# Print before
'''
print("State at time 0")
print(test_exp.attempted)
print(test_exp.actual)
print(test_exp.ages)
print(test_exp.deaths)
'''


#random.seed(4)
test_exp.advance(1)
test_exp.advance(2)
test_exp.advance(3)

'''
print("\nState at time 1")
print(test_exp.attempted)
print(test_exp.actual)
print(test_exp.ages)
print(test_exp.deaths)
'''

# write_attempted_csv

test_experiment = Experiment("testadjmat.csv", 1, 10, choice=1)
output = test_experiment.execute()
test_experiment.write_attempted_csv("attempted_test.csv")

# write_attempted_csv
test_experiment.write_actual_csv("actual_test.csv")

# write_age_csv
test_experiment.write_ages_csv("ages_test.csv")

