import random

#item classes
class world_break_scroll:
	def __init__(self, name):
		self.name = name
		self.call = "world break"

	def __repr__(self):
		return self.name

	def use(self):
		player.cmds[self.call] = world_break
		print("You have learned the world break skill!")

class potion:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name

	def use(self):
		x = random.randint(2, 5) + 4
		player.hp = player.hp + x
		print("You gained " + str(x) + " life!")

#this is the item dictionary
item_dict = {"world break scroll" : world_break_scroll, "potion" : potion}
