from Package import Package
from Container import Container
from Experiment import Experiment 
from Ensemble import Ensemble
import random
import numpy as np

def main():
	thresh_mouse_family = Ensemble("threshmouse.csv")
	thresh_mouse_family.ms_fill(50)

	N = thresh_mouse_family.N

	M = len(thresh_mouse_family.members)

	prefix = "thresh_family/thresh_mouse_rand_"
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