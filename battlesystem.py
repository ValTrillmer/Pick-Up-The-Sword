import random, time
from game_data import descriptors, names, creatures
from character import character
from sword import sword
from room import room



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
	
def create_player():
	p = character(creatures[0][0], creatures[0][1], creatures[0][2], creatures[0][3], creatures[0][4], creatures[0][5], creatures[0][6], creatures[0][7])
	return p


#this is the game

player = create_player()

room = room("dungeon", [], [], 0, True)
room.fill_chest()
room.add_enemy()
room.add_exit()
print(room)

print("You pick up a sword.")
new_sword = create_sword()
new_sword.view()
player.equip_sword(new_sword)

print("You have encountered a " + str(room.enemy))

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