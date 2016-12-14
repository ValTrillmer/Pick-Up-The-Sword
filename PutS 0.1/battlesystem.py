import random, time
from game_data import descriptors, names, creatures
from character import character
from sword import sword
from room import room
from generator import create_game



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
		if c in player.cmds.keys():
			k = player.cmds[c]()
			return k
			running = False
		else:
			pass

def ai_command():
	ai_go = True
	ai_list = []
	for key in room.enemy[0].cmds.keys():
		ai_list += [key]
	x = random.randint(0, len(ai_list) - 1)
	k = room.enemy[0].cmds[ai_list[x]](ai_go)
	return k



#starts game
create_game()

running = True
player_turn = True

while running:
	if len(room.enemy) == 0:
		player_turn = True
		player_turn = engine(player_turn)
	else:
		player_turn = engine(player_turn)
	player.check_alive()
	if len(room.enemy) == 0:
		pass
	else:
		room.enemy[0].check_alive()
		if room.enemy[0].alive == False:
			print("You are victorious!")
			room.enemy.pop(0)
	if player.alive == False:
		print("You have died.")
		running = False