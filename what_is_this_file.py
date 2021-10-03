from Package import Package
from Container import Container
from Experiment import Experiment
from Ensemble import Ensemble

def main():
	return

main()


from Experiment import Experiment
import os
import sys
import shutil


def make_activity_directory(in_file, dir_name, connectome, loads, t_min=0, choice=0):
	# Make the directory
	try:
		os.mkdir(dir_name)
	except FileExistsError:
		shutil.rmtree(dir_name)
		os.mkdir(dir_name)

	# Create the base of the file names
	choice_string = ["RW", "IS"]

	base = "dir_" + connectome + "_act_stats_" + choice_string[choice] + "_"

	for i in range(len(loads)):
		# get the name for the current file
		out_name = dir_name + "/" + base + str(i) + ".csv"
		# make an experiment
		exp = Experiment(in_file, loads[i], 1000, choice)
		
		# execute it
		exp.execute()

		# write the file
		exp.write_activity_1_csv(out_name, t_min)




def main():
	mouse_loads = [1, 2, 10, 21, 42]
	monkey91_loads = [1, 1, 4, 9, 18]
	cocomac_loads = [1, 1, 9, 18, 36]

	make_activity_directory("mouseunweighted.csv", "mouse_act_stats_RW", "mouse", mouse_loads, 100, choice=0)
	make_activity_directory("mouseunweighted.csv", "mouse_act_stats_IS", "mouse", mouse_loads, 100, choice=1)

	make_activity_directory("monkey91.csv", "monkey91_act_stats_RW", "monkey91", monkey91_loads, 100, choice=0)
	make_activity_directory("monkey91.csv", "monkey91_act_stats_IS", "monkey91", monkey91_loads, 100, choice=1)
	
	make_activity_directory("cocoadj.csv", "cocomac_act_stats_RW", "cocomac", cocomac_loads, 100, choice=0)
	make_activity_directory("cocoadj.csv", "cocomac_act_stats_IS", "cocomac", cocomac_loads, 100, choice=1)




main()