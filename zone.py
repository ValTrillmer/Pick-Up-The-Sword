class zone:
	def __init__(self, name, objects, population, corpse, interior):
		self.name = name
		self.objects = objects
		self.population = population
		self.corpse = corpse
		self.interior = interior

	def __repr__(self):
		return self.name