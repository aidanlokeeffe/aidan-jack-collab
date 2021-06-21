def advance(self, t):
	print("Last state: " + str(self.state))

	# Propagate the messages according to the chosen rule
	self.propagate(self.adj)
	print("Propogated: " + str(self.state))

	# Add the random messages after propagating
	new_message = Container(self.N)
	new_message.fill(t, self.load)
	print("Injection: " + str(new_message))

	self.state.incorporate(new_message)
	print("Post-injection: " + str(self.state))

	# Record everything as needed
	self.attempted.append( [len(self.state.contents[j].vals[0]) for j in range(self.N) ] )

	# Perform the collision, and record deaths
	doomed = []
	for j in range(self.N):
		arg1 = self.state.contents[j].vals[0]
		if len(arg1) > 1:
			arg2 = self.state.contents[j].vals[1]
			doomed.append( Package(arg1, arg2) )
			self.state.clear(j)
	self.deaths.append(doomed)

	self.actual.append( [len(self.state.contents[j].vals[0]) for j in range(self.N) ] )

	survivor_ages = []
	for j in range(self.N):
		try:
			survivor_ages.append( len(self.state.contents[j].vals[1][0]) )
		except IndexError:
			survivor_ages.append(0)

	self.ages.append(survivor_ages)