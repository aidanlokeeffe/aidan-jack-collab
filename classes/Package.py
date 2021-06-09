class Package(object):
	# val: int; tag: array of int; hist; array containing ONE array of integers
	def __init__(self, n=0, tag=[], hist=[[]]):
		self.val = [n, tag, hist]

	def __str__(self):
		return None

	def __repr__(self):
		return self.str()