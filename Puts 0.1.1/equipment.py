class sword:
	def __init__(self, name, blade, hilt, magic):
		self.name = name
		self.blade = blade
		self.hilt = hilt
		self.magic = magic

	def __repr__(self):
		return self.name + self.blade + self.hilt + self.magic

	def atk_bonus(self):
		return descriptors[self.blade] + descriptors[self.hilt] + descriptors[self.magic]



class armour:
	def __init__(self, name, material, craftsmanship, magic):
		self.name = name
		self.material = material
		self.craftsmanship = craftsmanship
		self.magic = magic

	def __repr__(self):
		return self.name + self.material + self.craftsmanship + self.magic

	def dfs.bonus(self):
		return descriptors[self.material] + descriptors[self.craftsmanship] + descriptors[self.magic]