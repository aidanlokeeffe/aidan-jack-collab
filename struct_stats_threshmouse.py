import os
import sys
import shutil
import numpy as np
import math
import networkx as nx
from Container import Container
from Package import Package
from Experiment import Experiment

def make_my_struct_stats(in_name, out_name):
	exp = Experiment(in_name, 1, 1000, 0)
	exp.write_structure_1_csv(out_name)




def main():
	'''
	in_names = ["thresh_er_comparison/thresh_mouse_er_0.csv", 
	            "thresh_er_comparison/thresh_mouse_er_1.csv"]
	out_names = ["thresh_er_0_anly/thresh_mouse_er_0_struct.csv",
	             "thresh_er_1_anly/thresh_mouse_er_1_struct.csv"]
	'''

	'''
	in_names = ["thresh_sf_comparison/thresh_mouse_sf_0.csv", 
	            "thresh_sf_comparison/thresh_mouse_sf_1.csv"]
	out_names = ["thresh_sf_0_anly/thresh_mouse_sf_0_struct.csv",
	             "thresh_sf_1_anly/thresh_mouse_sf_1_struct.csv"]
	'''

	in_names = ["thresh_family/thresh_mouse_rand_0.csv", 
	            "thresh_family/thresh_mouse_rand_1.csv"]
	out_names = ["thresh_ms_0_anly/thresh_mouse_ms_0_struct.csv",
	             "thresh_ms_1_anly/thresh_mouse_ms_1_struct.csv"]




	for i in range(len(in_names)):
		make_my_struct_stats(in_names[i], out_names[i])

main()