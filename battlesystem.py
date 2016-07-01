import random, time
from game_data import descriptors, names


#game classes
class character:
	def __init__(self, name, hp, dfs, atk, truth, inventory, a_inventory):
		self.name = name
		self.hp = hp
		self.dfs = dfs
		self.atk = atk
		self.alive = truth
		self.inventory = inventory
		self.a_inventory = a_inventory

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

	def use_item(self, p_commands):
		p_commands[self.inventory[0].call] = world_break
		list_commands()



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

class scroll:
	def __init__(self, name, call):
		self.name = name
		self.call = call

	def __repr__(self):
		return self.name

#engine functions
def engine(player_turn):
	if player_turn == True:
		turn = run_command()
		return turn
	else:
		turn = ai_command()
		return turn

def run_command():
	running  = True
	while running:
		c = input("> ")
		if c in p_commands.keys():
			k = p_commands[c]()
			return k
			running = False
		else:
			pass

def ai_command():
	ai_go = True
	ai_list = []
	for key in g_commands.keys():
		ai_list += [key]
	x = random.randint(0, len(ai_list) - 1)
	k = g_commands[ai_list[x]](ai_go)
	return k

#creates a sword
def create_sword():
	d_list = []
	for key in descriptors.keys():
		d_list += [key]
	descriptor_index1 = random.randint(0, len(d_list) - 1)
	descriptor_index2 = random.randint(0, len(d_list) - 1)
	descriptor_index3 = random.randint(0, len(d_list) - 1)
	name_index = random.randint(0, len(names) - 1)
	new_sword  = sword(names[name_index], d_list[descriptor_index1], d_list[descriptor_index2], d_list[descriptor_index3])
	return new_sword


#these are my commands

#receives input to determine which object to apply the damage toward
def attack(ai_go = False):
	#player's turn
	if ai_go == False:
		d = player.dmg_value()
		print("You attack for " + str(d) + " damage!")
		game.hp = game.hp - d + game.dfs
		return False
	#game turn
	else:
		d = game.dmg_value()
		print("you were attacked for " + str(d) + " damage!")
		player.hp = player.hp - d + player.dfs
		return True

def turtle(ai_go = False):
	#player's turn
	if ai_go == False:
		print("You have turtled")
		return False
	#game turn
	else:
		print("Your opponent has turtled")
		return True

def list_commands():
	commandlist = []
	for key in p_commands.keys():
		commandlist += [key]
	print(commandlist)
	return True

def heal(ai_go = False):
	l = random.randint(1,4)
	if ai_go == False:
		print("You gain " + str(l) + " life!")
		player.hp = player.hp + l
		return False
	else:
		print("Your opponent gained " + str(l) + " life!")
		game.hp = game.hp + l
		return True

def see_sword():
	print(player.a_inventory)
	print(new_sword.atk_bonus())
	return True

def world_break(ai_go = False):
	if ai_go == False:
		d = player.dmg_value() + 100
		print("You attack for " + str(d) + " damage!")
		time.sleep(1)
		print("Kablamo!!!")
		game.hp = game.hp + game.dfs - d
		return False
	else:
		d = game.dmg_value() + 100
		print("You were attacked for " + str(d) + " damage!")
		time.sleep(1)
		print("Kablamo!!!")
		player.hp = player.hp + player_turn.dfs - d
		return True

def grab_item(ai_go = False):
	if ai_go == False:
		print("A world break scroll was added to your inventory")
		world_break_scroll = scroll('world break', 'world break')
		player.add_inventory(world_break_scroll)
		print(player.inventory)
		return True
	else:
		return False

def use_scroll(ai_go = False):
	if ai_go == False:
		player.use_item(p_commands)
		return True
	else:
		return False

#these are the commands dictionaries
p_commands = {'attack' : attack, 'turtle' : turtle,
	'commands' : list_commands, 'heal' : heal,
	'see sword' : see_sword, 'grab item' : grab_item,
	'use scroll' : use_scroll}

g_commands = {'attack' : attack, 'turtle' : turtle,
	'heal' : heal}


#this is the game
player = character("you", 10, 2, 2, True, [], [])
game = character("game", 200, 2, 2, True, [], [])

print("You pick up a sword.")
new_sword = create_sword()
new_sword.view()
player.equip_sword(new_sword)

print("You have encountered an enemy")

running = True
player_turn = True

while running:
	player_turn = engine(player_turn)
	player.check_alive()
	game.check_alive()
	if player.alive == False:
		print("You have died.")
		running = False
	elif game.alive == False:
		print("You are victorious!")
		running = False