class Package(object):
	# val: int; tag: array of int; hist; 2D array, the inner arrays will contain integers
	# default is the empty package
	def __init__(self, n=0, tag=[], hist=[]):
		self.val = [n, tag, hist]

	def __add__(self, other):
		args = (self.val[_] + other.val[_] for _ in range(2))
		return Package(*args)

	def n(self):
		return self.val[0]

	def tag(self):
		return self.val[1]

	def hist(self):
		return self.val[2]