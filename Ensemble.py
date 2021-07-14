import random
import numpy as np
import math
import os
import sys
import shutil


class Ensemble(object):

	def __init__(self, adj=[[0]]):
		self.members = []

		if str(type(adj)) == "<class 'str'>":
			self.input_matrix(adj)
		else:
			# The other case is that the adjmat is pased as an array
			self.N = len(adj)
			self.seed = [[adj[i][j] for j in range(self.N)] for i in range(self.N)]

		self.num_iter = 0
		for i in range(self.N):
			for j in range(self.N):
				self.num_iter += int(self.seed[i][j])
		self.num_iter *= 100

	def input_matrix(self, inFile):
		matrix = np.genfromtxt(inFile, delimiter = ",")
		if math.isnan(matrix[0][0]):
			matrix = matrix[1:,1:]
		self.seed = matrix
		self.N = len(matrix)


	# This method takes a matrix, and performs one step of Maslov-Sneppen. It modifies mtx in
	# place, so do a deep copy of self.seed any time this is called
	def rewire(self, mtx):
		# Dummy check
		if id(mtx) == id(self.seed):
			print("Use a matrix with different memory than the seed matrix.")
			raise AssertionError

		abort_counter = 100000
		seeking = True

		while abort_counter > 0 and seeking:
			# Ranodmly choose i, and then j such that mtx[i][j] = 1
			i = random.sample(range(self.N), 1)[0]
			valid_j = [j for j in range(self.N) if mtx[i][j]]
			j = random.sample(valid_j, 1)[0]

			# Ranodmly choose k, and then l such that mtx[k][l] = 1
			k = random.sample(range(self.N), 1)[0]
			valid_l = [l for l in range(self.N) if mtx[k][l]]
			l = random.sample(valid_l, 1)[0]

			if (mtx[k][j]) or (mtx[i][l]):
				abort_counter -= 1
				continue

			mtx[i][j] = 0
			mtx[k][l] = 0
			mtx[k][j] = 1
			mtx[i][l] = 1
			seeking = False

		if abort_counter == 0:
			print("Aborted")
			raise AssertionError

	def ms_graph(self):
		member = [[self.seed[i][j] for j in range(self.N)] for i in range(self.N)]
		for _ in range(self.num_iter):
			self.rewire(member)
		self.members.append(member)

	def er_graph(self, nodes, prob):
		matrix = []
		for i in range(nodes):
			L=[0]*nodes
			for j in range(nodes):
				if j!=i:
					randy=random.random()
					if randy<prob:
						L[j]=1
			matrix.append(L)
		return matrix

	def er_graph_write(self, nodes, prob, out_name):
		graph = self.er_graph(nodes, prob)
		out_file = open(out_name, "w")
		st = ", "
		for i in range(nodes):
			st += str(i) + ", "
		out_file.write(st[:-2] + "\n")

		for i in range(nodes):
			st = str(i) + ", "
			for j in range(nodes):
				st += str(graph[i][j]) + ", "
			out_file.write(st[:-2] + "\n")

		out_file.close()

	def er_fill(self, amount, N, p):
		self.members=[]
		for k in range(amount):
			newbaby = self.er_graph(N, p)
			self.members.append(newbaby)
		return None

	def ms_fill(self, n):
		for _ in range(n):
			self.ms_graph()

	def write_ensemble_to_directory(self, dir_name, seed_name):
		# deal with the cases of the directory existing or not
		try:
			os.mkdir(dir_name)
		except FileExistsError:
			shutil.rmtree(dir_name)
			os.mkdir(dir_name)


		for k in range(len(self.members)):
			out_name = dir_name+"/"+seed_name+"_ensemble_elt_"+str(k)+".csv"
			out_file = open(out_name, "w")
			
			# write first line
			st = ", "
			for j in range(self.N):
				st += str(j) + ", "
			out_file.write(st[:-2]+ "\n")

			# write the rest of the lines
			for i in range(self.N):
				st = str(i) + ", "
				for j in range(self.N):
					st += str(self.members[k][i][j]) + ", "
				out_file.write(st[:-2] + "\n")

			# close the file
			out_file.close()



