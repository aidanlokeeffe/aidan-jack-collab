import random

class Ensemble(object):

	def __init__(self, adj):
		self.ensemble = []
		self.N = len(adj)
		self.seed = [ adj[i][j] for i in range(self.N) for j in range(self.N) ]

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
			i = random.sample(range(self.N), 1)
			valid_j = [j for j in range(self.N) if mtx[i][j]]
			j = random.sample(valid_j, 1)

			# Ranodmly choose k, and then l such that mtx[k][l] = 1
			k = random.sample(range(self.N), 1)
			valid_l = [l for l in range(self.N) if mtx[k][l]]
			l = random.sample(valid_l, 1)


			if (mtx[k][j]) or (mtx[i][l]):
				abort_counter -= 1
				continue

			mtx[i][j] = 0
			mtx[k][l] = 0
			mtx[k][j] = 1
			mtx[i][l] = 1
			seeking = False

	def create_member(self):
		member = [ self.seed[i][j] for i in range(self.N) for j in range(self.N) ]

		for _ in range(self.num_iter):
			self.rewire(member)

		self.ensemble.append(member)