import random

#item classes
class item:
	def __init__(self, name, func, reuseable):
		self.name = name
		self.func = func
		self.reuseable = reuseable

	def __repr__(self):
		return self.name
