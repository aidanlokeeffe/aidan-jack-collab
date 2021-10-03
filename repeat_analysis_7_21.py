import os
import sys
import shutil
import numpy as np
import math
import networkx as nx
from Container import Container
from Package import Package
from Experiment import Experiment

'''
def make_activity_directory(in_file, dir_name, connectome_name, loads, repetitions, t_min=0, choice=0):
	# Make the directory
	try:
		os.mkdir(dir_name)
	except FileExistsError:
		shutil.rmtree(dir_name)
		os.mkdir(dir_name)

	# Create the base of the file names
	choice_string = ["RW", "IS"]

	base = "dir_" + connectome_name + "_act_stats_" + choice_string[choice] + "_"

	for i in range(len(loads)):
		# get the name for the current file
		out_name = dir_name + "/" + base + str(i) + ".csv"
		# make an experiment
		exp = Experiment(in_file, loads[i], 1000, choice)
		
		# execute it
		exp.execute()

		# write the file
		exp.write_activity_1_csv(out_name, t_min)
'''


# This function need to store all the shit in an array
def make_activity_directory(in_file, dir_name, connectome_name, loads, repetitions, t_min=0, choice=0):
	# Make the directory
	try:
		os.mkdir(dir_name)
	except FileExistsError:
		shutil.rmtree(dir_name)
		os.mkdir(dir_name)

	# Create the base of the file names
	choice_string = ["RW", "IS"]

	base =  connectome_name + "_act_stats_" + choice_string[choice] + "_"

	for i in range(len(loads)):
		# Get all the data needed
		influence_trials = []
		redundancy_trials = []
		avgdeathage_trials = []

		# Perform the required number of repetitions 
		for j in range(repetitions):
			exp = Experiment(in_file, loads[i], 1000, choice)
			exp.execute()
			influence_trials.append(exp.influence_values(t_min))
			redundancy_trials.append(exp.redundancy_values(t_min))
			avgdeathage_trials.append(exp.age_at_death_values(t_min))

		# Get the means 
		influence_mean_dict = { k: np.mean( [influence_trials[_][k] for _ in range(repetitions)]) for k in range(exp.N) }
		redundancy_mean_dict = { k: np.mean( [redundancy_trials[_][k] for _ in range(repetitions)]) for k in range(exp.N) }
		avgdeathage_mean_dict = { k: np.mean( [avgdeathage_trials[_][k] for _ in range(repetitions)]) for k in range(exp.N) }

		# Get the standard deviations too
		influence_std_dict = { k: np.std( [influence_trials[_][k] for _ in range(repetitions)]) for k in range(exp.N) }
		redundancy_std_dict = { k: np.std( [redundancy_trials[_][k] for _ in range(repetitions)]) for k in range(exp.N) }
		avgdeathage_std_dict = { k: np.std( [avgdeathage_trials[_][k] for _ in range(repetitions)]) for k in range(exp.N) }


		# Make yet another dictionary with all the values that will go on a given line
		line_dict = { k: [influence_trials[_][k] for _ in range(repetitions)] + [influence_mean_dict[k]] + [influence_std_dict[k]] + [redundancy_trials[_][k] for _ in range(repetitions)] + [redundancy_mean_dict[k]] + [redundancy_std_dict[k]] + [avgdeathage_trials[_][k] for _ in range(repetitions)] + [avgdeathage_mean_dict[k]] + [avgdeathage_std_dict[k]] for k in range(exp.N) }

		# Get the name for the current file
		out_name = dir_name + "/" + base + str(i) + ".csv"

		# Get the header
		header = ", "
		for k in range(repetitions):
			header += "influence_" + str(k) + ", "
		header += "influence_mean, "
		header += "influence_std, "
		for k in range(repetitions):
			header += "redundancy_" + str(k) + ", "
		header += "redundancy_mean, "
		header += "redundancy_std, "
		for k in range(repetitions):
			header += "avgdeathage_" + str(k) + ", "
		header += "avgdeathage_mean, "
		header += "avgdeathage_std\n"


		# Write the output
		out_file = open(out_name, "w")
		out_file.write(header)

		for j in range(exp.N):
			st = str(j) +", "
			for word in line_dict[j]:
				st += str(word) + ", "
			out_file.write(st[:-2] + "\n")

		out_file.close()








def main():
	mouse_loads = [1, 2, 10, 21, 42]
	monkey91_loads = [1, 1, 4, 9, 18]
	cocomac_loads = [1, 1, 9, 18, 36]

	'''
	make_activity_directory("threshmouse.csv", "repeat_threshmouse_RW", "threshmouse", mouse_loads, 20, 100, choice=0)
	make_activity_directory("threshmouse.csv", "repeat_threshmouse_IS", "threshmouse", mouse_loads, 20, 100, choice=1)

	make_activity_directory("monkey91.csv", "repeat_monkey91_RW", "monkey91", monkey91_loads, 20, 100, choice=0)
	make_activity_directory("monkey91.csv", "repeat_monkey91_IS", "monkey91", monkey91_loads, 20, 100, choice=1)
	
	make_activity_directory("cocoadj.csv", "repeat_cocomac_RW", "cocomac", cocomac_loads, 20, 100, choice=0)
	make_activity_directory("cocoadj.csv", "repeat_cocomac_IS", "cocomac", cocomac_loads, 20, 100, choice=1)
	'''

	# Despite my horrible naming of this file, I'm just gonna reuse it, because its perfectly 
	# good. Hence, we'll just comment out the code above, to preseve the data we have already.

	'''
	in_names = ["thresh_er_comparison/thresh_mouse_er_0.csv", 
	            "thresh_er_comparison/thresh_mouse_er_1.csv"]
	out_names = ["thresh_er_0_anly/thresh_mouse_er_0_struct.csv",
	             "thresh_er_1_anly/thresh_mouse_er_1_struct.csv"]

	in_names = ["thresh_sf_comparison/thresh_mouse_sf_0.csv", 
	            "thresh_sf_comparison/thresh_mouse_sf_1.csv"]
	out_names = ["thresh_sf_0_anly/thresh_mouse_sf_0_struct.csv",
	             "thresh_sf_1_anly/thresh_mouse_sf_1_struct.csv"]

	in_names = ["thresh_family/thresh_mouse_rand_0.csv", 
	            "thresh_family/thresh_mouse_rand_1.csv"]
	out_names = ["thresh_ms_0_anly/thresh_mouse_ms_0_struct.csv",
	             "thresh_ms_1_anly/thresh_mouse_ms_1_struct.csv"]
	'''

	# ER MOUSE 0
	# make_activity_directory("thresh_er_comparison/thresh_mouse_er_0.csv", "thresh_er_0_RW", "mouse_er_0", mouse_loads, 20, 100, choice=0)
	make_activity_directory("thresh_er_comparison/thresh_mouse_er_0.csv", "thresh_er_0_anly/thresh_er_0_IS", "mouse_er_0", mouse_loads, 20, 100, choice=1)

	# ER MOUSE 1
	make_activity_directory("thresh_er_comparison/thresh_mouse_er_1.csv", "thresh_er_1_anly/thresh_er_1_RW", "mouse_er_1", mouse_loads, 20, 100, choice=0)
	make_activity_directory("thresh_er_comparison/thresh_mouse_er_1.csv", "thresh_er_1_anly/thresh_er_1_IS", "mouse_er_1", mouse_loads, 20, 100, choice=1)

	# MS MOUSE 0
	make_activity_directory("thresh_family/thresh_mouse_rand_0.csv", "thresh_ms_0_anly/thresh_ms_0_RW", "mouse_ms_0", mouse_loads, 20, 100, choice=0)
	make_activity_directory("thresh_family/thresh_mouse_rand_0.csv", "thresh_ms_0_anly/thresh_ms_0_IS", "mouse_ms_0", mouse_loads, 20, 100, choice=1)

	# MS MOUSE 1
	make_activity_directory("thresh_family/thresh_mouse_rand_1.csv", "thresh_ms_1_anly/thresh_ms_1_RW", "mouse_ms_1", mouse_loads, 20, 100, choice=0)
	make_activity_directory("thresh_family/thresh_mouse_rand_1.csv", "thresh_ms_1_anly/thresh_ms_1_IS", "mouse_ms_1", mouse_loads, 20, 100, choice=1)

	# SF MOUSE 0
	make_activity_directory("thresh_sf_comparison/thresh_mouse_sf_0.csv", "thresh_sf_0_anly/thresh_sf_0_RW", "mouse_sf_0", mouse_loads, 20, 100, choice=0)
	make_activity_directory("thresh_sf_comparison/thresh_mouse_sf_0.csv", "thresh_sf_0_anly/thresh_sf_0_IS", "mouse_sf_0", mouse_loads, 20, 100, choice=1)

	# SF MOUSE 1
	make_activity_directory("thresh_sf_comparison/thresh_mouse_sf_1.csv", "thresh_sf_1_anly/thresh_sf_1_RW", "mouse_sf_1", mouse_loads, 20, 100, choice=0)
	make_activity_directory("thresh_sf_comparison/thresh_mouse_sf_1.csv", "thresh_sf_1_anly/thresh_sf_1_IS", "mouse_sf_1", mouse_loads, 20, 100, choice=1)





main()