from Package import Package

class Pitstop(object):
	# No default
	def __init__(self, f1, f2, f3):
		self.funcs = [f1, f2, f3]

	def apply(self, pkg):
		args = ( self.funcs[_](pkg.vals[_]) for _ in range(2))
		return Package(*args)