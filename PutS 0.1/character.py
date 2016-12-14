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

	def set_commands(self):
		if self.name == "player":
			self.cmds = {'attack' : self.attack, 'commands' : self.list_commands, 'see sword' : self.see_sword}
		else:
			self.cmds = {'attack' : self.attack}

	#items items to invetory
	def add_inventory(self, item):
		self.inventory.append(item)

	#equips sword
	def equip_sword(self, new_sword):
		if len(self.a_inventory) == 0:
			self.a_inventory.append(new_sword)
		else:
			self.inventory.append(new_sword)

	#determines base damage value
	def dmg_value(self):
		if len(self.a_inventory) == 0:
			return self.atk + random.randint(0, 6)
		else:
			return self.atk + random.randint(0, 6) + self.a_inventory[0].atk_bonus()

	#shows sword and its attack value
	def see_sword(self):
		print(self.a_inventory)
		print(new_sword.atk_bonus())
		return True

	#character commands
	def attack(self, ai_go = False):
		#player's turn
		if ai_go == False:
			d = player.dmg_value()
			print("You attack for " + str(d) + " damage!")
			room.enemy[0].hp = room.enemy[0].hp - d + room.enemy[0].dfs
			return False
		#game turn
		else:
			d = room.enemy[0].dmg_value()
			print("you were attacked for " + str(d) + " damage!")
			player.hp = player.hp - d + player.dfs
			return True

	def list_commands():
		commandlist = []
		for key in player.cmds.keys():
			commandlist += [key]
		print(commandlist)
		return True

	#def use(self, p_commands, ai_go = False):

	#def grab(ai_go = False):

	#def drop(ai_go = False):

	#def search(ai_go = False):