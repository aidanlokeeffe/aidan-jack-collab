from Package import Package
from Container import Container
from Experiment import Experiment 
from Ensemble import Ensemble
import random
import numpy as np

# This function takes a 3-D array and returns a 2-D array whose (i,j)-th entry
# is the average of the fiber (i,j,k) over k
# We assume that all rows of the array are the same length, and also that there
# is at least one entry
def average_across_pages(three_arr):
	out = []
	num_pages = len(three_arr)
	num_rows = len(three_arr[0])
	num_cols = len(three_arr[0][0])

	for j in range(num_rows):
		row = []
		for k in range(num_cols):
			val = 0
			for i in range(num_pages):
				val += three_arr[i][j][k]
			row.append( val / num_pages )
		out.append(row)
	return out


# NOTE THAT YOUR CODE DOES NOT THR
def age_hypo_tests(in_file, ensbl_size, load, T, j_min=0, repetitions=1, choice=0):
	# Do the experiment on the actual connectome as many times as specified
	observations = []
	for _ in range(repetitions):
		exp = Experiment(in_file, load, T, choice)
		exp.execute()
		observations.append(exp.summarize_visitation_data(j_min))

	# Average over the pages
	observations = average_across_pages(observations)

	# Make an ensemble of the specified size
	ensbl = Ensemble(in_file)
	ensbl.ms_fill(ensbl_size)

	# Get the distributions of each 6 number summary of each of the three 
	# statistics. This will be another 3-D array
	ensemble_simulations = []
	for member in ensbl.members:
		observations = []
		for _ in range(repetitions):
			exp = Experiment(in_file, load, T, choice)
			exp.execute()
			observations.append(exp.summarize_visitation_data(j_min))
		observations = average_across_pages(observations)
		ensemble_simulations.append(observations)

	# Do all the 
	out = []
	for j in range(6):
		for k in range(3):
			fiber = []
			for i in range(ensbl_size):
				fiber.append(ensemble_simulations[i][j][k])
			pL = len(list(filter(lambda x: x < observations[j][k], fiber))) / ensbl_size
			pR = len(list(filter(lambda x: x < observations[j][k], fiber))) / ensbl_size
			out.append((pL,pR))

	return out


def main():
	test_adj = [[0,1,0,0,1],
	            [1,0,0,1,1],
	            [0,1,0,1,0],
	            [0,0,1,0,0],
	            [1,1,1,1,0]]

	#results = age_hypo_tests("testadjmat.csv", 100, 1, 1000, 100, 10, 0)
	#print(results)

	# REMEMBER THAT YOU NEED TO INCORPORATE JACK'S FIX BEFORE YOU CAN DO CHOICE = 0, AS YOU LEARNED THE HARD WAY
	#results = age_hypo_tests("connectome_of_interest.csv", 5, 0.1*N, 1000, 100, 10, 1)
	#SAMPLE CALL: age_hypo_tests(in_file, ensbl_size, load, T, j_min=0, repetitions=1, choice=0)

	results = age_hypo_tests("monkey91.csv", 5, 9, 1000, 100, 10, 1)

	print(results)
















	# THE PROCEDURE
	# 1) Get the stats I need from the mouse connectome
	# 2) Generate an ensemble from the mouse connectome (HOW BIG?!)
	# 3) Get the distribution of the stats above 
	# 4) Do the hypothesis tests dammit!

	# THE PROCEDURE NOW
	# 0) Take all the parameters
	# 0.5) Make the ensemble
	# 1) Do 10 experiments on the given connectome, and average all the results
	# 2) For each ensemble element, do 10 experiments, and then average those too, and store them in a 3-D array
	# 3) Do both one sided hypothesis tests


	# First, we do the tests under random walk





	# Then, we do this for 
	





	# Then we do the tests under information spreading







	# Is there anything else that we have to do?
	

main()