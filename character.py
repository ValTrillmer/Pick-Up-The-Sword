import random
from game_data import creatures

class character:
	def __init__(self, name, hp, dfs, atk, truth, inventory, a_inventory, cmds):
		self.name = name
		self.hp = hp
		self.dfs = dfs
		self.atk = atk
		self.alive = truth
		self.inventory = inventory
		self.a_inventory = a_inventory
		self.cmds = cmds

	def __repr__(self):
		return self.name

	def check_alive(self):
		if self.hp < 1:
			self.alive = False

	#items items to invetory
	def add_inventory(self, item):
		self.inventory.append(item)

	#equips sword
	def equip_sword(self, new_sword):
		if len(self.a_inventory) == 0:
			self.a_inventory.append(new_sword)
		else:
			self.inventory.append(new_sword)

	def dmg_value(self):
		if len(self.a_inventory) == 0:
			return self.atk + random.randint(0, 6)
		else:
			return self.atk + random.randint(0, 6) + self.a_inventory[0].atk_bonus()

	def use_item(self, p_commands, ai_go):
		if ai_go == False:
			options = {}
			z = 0
			for self.inventory[z] in self.inventory:
				if z < len(self.inventory):
					options[z+1] = self.inventory[z]
					z = z+1
			print(options)
			x = input("Choose item\n> ")
			self.inventory[int(x)-1].use()
			del(self.inventory[int(x)-1])
		else:
			pass