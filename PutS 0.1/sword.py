from game_data import descriptors

class sword:
	def __init__(self, name, blade, hilt, magic):
		self.name = name
		self.blade = blade
		self.hilt = hilt
		self.magic = magic

	def __repr__(self):
		return self.name

	def view(self):
		print("The sword is called " + self.name + ". Its blade is " + self.blade + ". Its hilt is " + self.hilt + ". Its magic is " + self.magic + ".")

	def atk_bonus(self):
		return descriptors[self.blade] + descriptors[self.hilt] + descriptors[self.magic]