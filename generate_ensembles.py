# THIS FILE TAKES ALL OF THE DESIRED CONNECTOMES, AND 
# GENERATES A BIG FAMILY OF RANDOM GRAPHS. WE DO THIS 
# HERE INSTEAD OF DOING IT EVERY TIME WE RUN THE HYPOTHESIS
# TESTS, BECAUSE IT WOULD BE A WASTE OF TIME TO MAKE A NEW FAMILY 
# EVERYTIME, WE CAN JUST TAKE SUBSETS OF THE BIG ENSEMBLES 
# GENERATED HERE


from Package import Package
from Container import Container
from Experiment import Experiment 
from Ensemble import Ensemble
import random
import numpy as np
import time

# Make me 20,000 Maslov-Sneppen graphs from each connectome
def main():
	M = 5

	mouse = "mouseunweighted.csv"
	mouse_esbl = Ensemble(mouse)
	t0 = time.time()
	mouse_esbl.ms_fill(M)
	tf = time.time()
	print("MS takes " + str(tf - t0) + " seconds to make a " + str(M) + " member ensemble from the mouse connectome")
	mouse_esbl.write_ensemble_to_directory("mouse_rand", "mouseunweighted")

	monkey91 = "monkey91.csv"
	monkey91_esbl = Ensemble(monkey91)
	t0 = time.time()
	monkey91_esbl.ms_fill(M)
	tf = time.time()
	print("MS takes " + str(tf - t0) + " seconds to make a " + str(M) + " member ensemble from the monkey91 connectome")
	monkey91_esbl.write_ensemble_to_directory("monkey91_rand", "monkey91")

main()