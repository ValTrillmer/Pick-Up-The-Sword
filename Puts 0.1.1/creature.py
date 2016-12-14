class creature:
	def __init__(self, alive, name, hp, dfs, atk, inv, weapon, armour, cmds):
		self.name = name
		self.alive = alive
		self.hp = hp
		self.dfs = dfs
		self.atk = atk
		self.inv = inv
		self.weapon = weapon
		self.armour = armour
		self.cmds = cmds

	def __repr__(self):
		return self.name