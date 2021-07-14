from Package import Package
from Container import Container
from Experiment import Experiment
import math
import random
import time
import numpy as np

def make_N_L_pairs():
	out = []
	for N in [10, 50, 100, 200, 400]:
		row = []
		for L in [1, 0.01, 0.05, 0.1, 0.2, 0.5]:
			if L == 1:
				row.append( (N, L) )
				continue
			row.append((N, max([1, math.floor(L*N)])))
		out.append(row)
	return out

def get_runtime_of_execute(N,L,choice):
	print((N,L))
	# Get the file name
	in_file = "er_" + str(N) + ".csv"

	runtimes = []
	for _ in range(1):
		# make a new experiment
		exp = Experiment(in_file, L, 1000, choice)

		# get the starting time
		t0 = time.time()

		# execute
		exp.execute()

		# get the finishing time
		tf = time.time()

		# record the elapsed time 
		runtimes.append(tf-t0)

	return np.mean(runtimes)



def main():
	
	''' CHECKING THAT make_N_L_pairs WORKS
	pairs = make_N_L_pairs()
	for row in pairs:
		print(row)
	IT DOES '''

	'''
	results = [ ["(N,L)", "ONE", 0.01, 0.05, 0.1, 0.2, 0.5],
	            [10],
	            [50],
	            [100],
	            [200],
	            [400] ]  
	choice = 0
	pairs = make_N_L_pairs()
	for i in range(len(pairs)):
		for j in range(len(pairs[i])):
			results[i+1].append(  get_runtime_of_execute(pairs[i][j][0], pairs[i][j][1], choice) )

	print("Choice: " + str(choice))
	for row in results:
		print(row)
	'''

	print()

	results = [ ["(N,L)", "ONE", 0.01, 0.05, 0.1, 0.2, 0.5],
	            [10],
	            [50],
	            [100],
	            [200],
	            [400] ]  
	choice = 1
	pairs = make_N_L_pairs()
	for i in range(len(pairs)):
		for j in range(len(pairs[i])):
			results[i+1].append(  get_runtime_of_execute(pairs[i][j][0], pairs[i][j][1], choice) )

	print("Choice: " + str(choice))
	for row in results:
		print(row)

main()