import random

descriptors = 'funny sharp dull snakes powerful gleeming wobbly ugly golden rakish silver furry yucky slimy smelly rusty mysterious'.split()
names = "thwacker poop bully whimpy destructor crumble notverygood".split()

class character:
	def __init__(self, name, hp, truth, inventory):
		self.name = name
		self.hp = hp
		self.alive = truth
		self.inventory = inventory

	def check_alive(self):
		if self.hp < 1:
			self.alive = False

	def add_inventory(self, new_sword):
		self.inventory.append(new_sword)


class sword:
	def __init__(self, name, blade, hilt, magic):
		self.name = name
		self.blade = blade
		self.hilt = hilt
		self.magic = magic

	def view(self):
		print("The sword is called  " + self.name + ". Its blade is " + self.blade + ". Its hilt is " + self.hilt + ". Its magic is " + self.magic + ".")

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
		if c in commands.keys():
			k = commands[c]()
			return k
			running = False
		else:
			pass

def ai_command():
	ai_go = True
	x = random.randint(1,3)
	if x == 1:
		k = attack(ai_go)
		return k
	elif x == 2:
		k = turtle(ai_go)
		return k
	else:
		k = heal(ai_go)
		return k

def create_sword():
	descriptor_index1 = random.randint(0, len(descriptors) - 1)
	descriptor_index2 = random.randint(0, len(descriptors) - 1)
	descriptor_index3 = random.randint(0, len(descriptors) - 1)
	name_index = random.randint(0, len(names) - 1)
	new_sword  = sword(names[name_index], descriptors[descriptor_index1], descriptors[descriptor_index2], descriptors[descriptor_index3])
	return new_sword


#these are my commands

#receives input to determine which object to apply the damage toward
def attack(ai_go = False):
	#player's turn
	if ai_go == False:
		d = random.randint(0, 6)
		print("You attack for " + str(d) + " damage!")
		game.hp = game.hp - d
		return False
	#game turn
	else:
		d = random.randint(0, 6)
		print("you were attacked for " + str(d) + " damage!")
		player.hp = player.hp - d
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
	for key in commands.keys():
		commandlist += [key]
	commandlist.sort()
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

commands = {'attack' : attack, 'turtle' : turtle,
	'commands' : list_commands, 'heal' : heal}


#this is the game





player = character("you", 10, True, [])
game = character("game", 10, True, [])

print("You pick up a sword.")
new_sword = create_sword()
new_sword.view()
player.add_inventory(new_sword)

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