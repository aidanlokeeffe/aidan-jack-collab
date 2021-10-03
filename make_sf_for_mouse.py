import os
import sys
import shutil
import numpy as np
import math
import networkx as nx
from Container import Container
from Package import Package
from Experiment import Experiment
from Ensemble import Ensemble


def main():
	thresh_mouse_family = Ensemble("threshmouse.csv")
	#alpha, beta, delta_in, delta_out, make_simple = True
	thresh_mouse_family.sf_fill(100, 212, 0.014885, 0.97023, 1, 1)

	#0.014791, 0.985209

	N = thresh_mouse_family.N
	M = len(thresh_mouse_family.members)

	prefix = "thresh_sf_comparison/thresh_mouse_sf_"
	for i in range(M):
		out_file = open(prefix + str(i) + ".csv", "w")

		# write header
		st = ", "
		for j in range(N):
			st += str(j) + ", "
		out_file.write(st[:-2] + "\n")

		# write every line to the csv
		for j in range(N):
			st = str(j) +", "
			for k in range(N):
				st += str(thresh_mouse_family.members[i][j][k]) + ", "
			out_file.write(st[:-2] + "\n")

		out_file.close()

main()