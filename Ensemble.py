import random

class Ensemble(object):

	def __init__(self, adj):
		self.members = []
		self.N = len(adj)
		self.seed = [[adj[i][j] for j in range(self.N)] for i in range(self.N)]

		self.num_iter = 0
		for i in range(self.N):
			for j in range(self.N):
				self.num_iter += adj[i][j]
		self.num_iter *= 100


	# This method takes a matrix, and performs one step of Maslov-Sneppen. It modifies mtx in
	# place, so do a deep copy of self.seed any time this is called
	def rewire(self, mtx):
		# Dummy check
		if id(mtx) == id(self.seed):
			print("Use a matrix with different memory than the seed matrix.")
			raise AssertionError

		abort_counter = 100
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

	def new_member(self):
		member = [[self.seed[i][j] for j in range(self.N)] for i in range(self.N)]
		for _ in range(self.num_iter):
			self.rewire(member)
		self.members.append(member)

	def er_graph(self,nodes,probability):
    L = [0]*nodes
    matrix=[]
    for n in range(nodes):
        matrix.append(L)
    for i in range(nodes):
        for j in range(nodes):
            if i==j:
                matrix[i][j]=0
            else:
                randy = random.random()
                if randy>probability:
                    matrix[i][j]=1
                else:
                    matrix[i][j]=0
    return matrix

	def er_fill(self, amount, nodes, prob):
		self.members=[]
		for k in range(amount):
			newbaby = self.er_graph(nodes, prob)
			self.members.append(newbaby)

		

	def ms_fill(self, n):
		for _ in range(n):
			self.new_member()