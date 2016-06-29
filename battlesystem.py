import random

class character:
	def __init__(self, name, hp, truth):
		self.name = name
		self.hp = hp
		self.alive = truth

	def check_alive(self):
		if self.hp < 1:
			self.alive = False

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

#these are my commands

#receives input to determine which object to apply the damage toward
def attack(ai_go = False):
	d = random.randint(0, 6)
	#player's turn
	if ai_go == False:
		print("You attack for " + str(d) + " damage!")
		game.hp = game.hp - d
		return False
	#game turn
	else:
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

player = character("you", 10, True)
game = character("game", 10, True)

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