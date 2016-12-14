class room:
	def __init__(self, name, chest, entity, exit):
		self.name = name
		self.chest = chest
		self.entity = entity
		self.exit = exit

	def __repr__(self):
		return self.name + " " + str(self.chest) + " " + str(self.enemy)