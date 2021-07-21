from Package import Package
from Container import Container
from Experiment import Experiment
import math
import random
import time
import numpy as np

# As it exists, this program is shit

def time_execute(exp):
	t0 = time.time()
	exp.execute()
	tf = time.time()
	return tf-t0

def main():
	mouse_times_RW = []
	monkey91_times_RW = []
	cocomac_times_RW = []
	mouse_times_IS = []
	monkey91_times_IS = []
	cocomac_times_IS = []
	for _ in range(50):
		# (fileName, load, T, choice=0)
		mouse_exp_RW = Experiment("mouseunweighted.csv", 21, 1000, 0)
		monkey91_exp_RW = Experiment("monkey91.csv", 9, 1000, 0)
		cocomac_exp_RW = Experiment("cocoadj.csv", , 1000, 0)
		mouse_exp_IS = Experiment("mouseunweighted.csv", 21, 1000, 1)
		monkey91_exp_IS = Experiment("monkey91.csv", 9, 1000, 1)
		cocomac_exp_IS = Experiment("cocoadj.csv", , 1000, 1)

		mouse_times_RW.append(time_execute(mouse_exp_RW))
		monkey91_times_RW.append(time_execute(monkey91_exp_RW))
		cocomac_times_RW.append(time_execute(cocomac_exp_RW))
		mouse_times_IS.append(time_execute(mouse_exp_IS))
		monkey91_times_IS.append(time_execute(monkey91_exp_IS))
		cocomac_times_IS.append(time_execute(cocomac_exp_IS))

	print("On average, RW on mouse takes " + str( np.mean(mouse_times_RW) ) + " seconds to execute.")
	print("On average, RW monkey91 takes " + str( np.mean(monkey91_times_RW) ) + " seconds to execute.")
	print("On average, RW cococac takes " + str( np.mean(cocomac_times_RW) ) + " seconds to execute.")
	print("On average, IS on mouse takes " + str( np.mean(mouse_times_IS) ) + " seconds to execute.")
	print("On average, IS monkey91 takes " + str( np.mean(monkey91_times_IS) ) + " seconds to execute.")
	print("On average, IS cococac takes " + str( np.mean(cocomac_times_IS) ) + " seconds to execute.")

main()



















'''
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
	
	 CHECKING THAT make_N_L_pairs WORKS
	pairs = make_N_L_pairs()
	for row in pairs:
		print(row)
	IT DOES 

	
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
'''