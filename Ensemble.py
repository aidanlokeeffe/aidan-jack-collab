import random
import numpy as np
import math

class Ensemble(object):

	def __init__(self, adj):
		self.members = []
		

		if str(type(adj)) == "<class 'str'>":
			self.input_matrix(adj)
		else:
			self.seed = [[adj[i][j] for j in range(self.N)] for i in range(self.N)]
			self.N = len(adj)

		self.num_iter = 0
		for i in range(self.N):
			for j in range(self.N):
				self.num_iter += self.seed[i][j]
		self.num_iter *= 100
		self.num_iter = int(self.num_iter)
		print(self.num_iter)



	def input_matrix(self, inFile):
		matrix = np.genfromtxt(inFile, delimiter = ',')
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

		abort_counter = 10000
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

	def sf_graph(self, N, alpha, beta, delta_in, delta_out, make_simple = True):
		# Make a list of the nodes
		nodes = [i for i in range(N)]

		# Get gamma
		gamma = 1 - alpha - beta

		# Initialize the adjacency matrix
		out = np.zeros((N,N))

		# The seed graph has to have at least one edge
		out[0,1] = 1

		# There is a 50-50 chance of the seed graph having two edges
		out[1,0] = random.randint(0,1)

		# Initialize the node counter
		n=2

		# Initialize the edge counter
		e = sum(sum(out))

		# Set up the in degree and out degree counters
		in_deg = np.sum(out, axis=0)
		out_deg = np.sum(out, axis=1)

		# Set up the from and to probs
		from_probs = [ (out_deg[i] + delta_out)/(e + delta_out*n) for i in range(N) ]
		to_probs = [ (in_deg[j] + delta_in)/(e + delta_in*n) for j in range(N) ]

		# LOOP THAT BUILDS GRAPH
		while n < N:
			# Figure out which action to take
			action = random.choices([0,1,2], [alpha,beta,gamma], k=1)[0]

			if action == 0:
				# Add a new node, and connect it to an existing edge at random
				to_node = random.choices(nodes, to_probs, k=1)[0]
				out[n, to_node] += 1
				n += 1
			elif action == 1:
				# Add a new edge between existing nodes
				to_node = random.choices(nodes, to_probs, k=1)[0]
				from_node = random.choices(nodes, from_probs, k=1)[0]
				out[from_node, to_node] += 1
			else:
				# Add a new node, and connect an existing node to it
				from_node = random.choices(nodes, from_probs, k=1)[0]
				out[from_node, n] += 1
				n += 1
			# In all cases, we have added exactly one edge
			e += 1

			# Update the degree sequences and corresponding probabilities
			in_deg = np.sum(out, axis=0)
			out_deg = np.sum(out, axis = 1)

			from_probs = [ (out_deg[i] + delta_out)/(e + delta_out*n) for i in range(N) ]
			to_probs = [ (in_deg[j] + delta_in)/(e + delta_in*n) for j in range(N) ]

		# Finally, make it simple if needed
		if make_simple:
			for i in range(N):
				for j in range(N):
					if i==j:
						out[i,j] = 0
						continue
					out[i,j] = min(out[i,j], 1)

		C = e / N / (N-1)
		print("Connection Density is " + str(C))
		return out








	def er_fill(self, amount, N, p):
		self.members=[]
		for k in range(amount):
			newbaby = self.er_graph(N, p)
			self.members.append(newbaby)
		return None

	def ms_fill(self, amount):
		for _ in range(amount):
			self.ms_graph()

	def sf_fill(self, amount, N, alpha, beta, delta_in, delta_out, make_simple = True):
		for _ in range(amount):
			self.members.append(self.sf_graph(N, alpha, beta, delta_in, delta_out, make_simple))