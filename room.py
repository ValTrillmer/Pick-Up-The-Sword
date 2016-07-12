import random
from character import character
from game_data import creatures
from item import item_dict

class room:
	def __init__(self, name, chest, enemy, exit, player_in):
		self.name = name
		self.chest = chest
		self.enemy = enemy
		self.exit = exit
		self.player_in = player_in

	def __repr__(self):
		return self.name + " " + str(self.chest) + " " + str(self.enemy)

	def fill_chest(self):
		chest_inv = random.randint(0,3)
		y = 0
		item_list = []
		for key in item_dict.keys():
			item_list += [key]
		empty = True
		while empty:
			if y <= chest_inv:
				x = random.randint(0, len(item_list) - 1)
				item = item_dict[item_list[x]](item_list[x])
				self.chest.append(item)
				y = y + 1
			else:
				empty = False

	def add_enemy(self):
		c = []
		for key in creatures.keys():
			c += [key]
		new_creature = random.randint(1, len(c) - 1)
		cr = c[new_creature]
		ghoul = character(creatures[cr][0], creatures[cr][1], creatures[cr][2], creatures[cr][3], creatures[cr][4], creatures[cr][5], creatures[cr][6], creatures[cr][7])
		self.enemy.append(ghoul)

	def add_exit(self):
		self.exit = random.randint(1,3)