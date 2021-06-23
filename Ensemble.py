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

		# Ranodmly choose i, and then j such that mtx[i][j] = 1
		# Ranodmly choose k, and then l such that mtx[k][l] = 1

		if (mtx[k][j]) or (mtx[i][l]):
			continue

		mtx[i][j] = 0
		mtx[k][l] = 0
		mtx[k][j] = 1
		mtx[i][l] = 1

	def create_member(self):
		member = [ self.seed[i][j] for i in range(self.N) for j in range(self.N) ]

		# Get the number of rewirings needed

		# Rewire that many times

		# Append to ensemble