import random

#these are my commands

#receives input to determine which object to apply the damage toward
def attack(ai_go = False):
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
	for key in player.cmds.keys():
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
		room.enemy[0].hp = room.enemy[0].hp + l
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
		enemy.hp = enemy.hp + enemy.dfs - d
		return False
	else:
		d = enemy.dmg_value() + 100
		print("You were attacked for " + str(d) + " damage!")
		time.sleep(1)
		print("Kablamo!!!")
		player.hp = player.hp + player_turn.dfs - d
		return True

def grab_item(ai_go = False):
	if ai_go == False:
		item_list = []
		for key in item_dict.keys():
			item_list += [key]
		x = random.randint(0, len(item_list) - 1)
		item_list[x] = item_dict[item_list[x]](item_list[x])
		player.add_inventory(item_list[x])
		print("A " + str(item_list[x]) + " was added to your inventory.")
		print(player.inventory)
		return True
	else:
		return False

def use_item(ai_go = False):
	if ai_go == False:
		player.use_item(player.cmds, ai_go)
		return True
	else:
		return False

def search_chest(ai_go = False):
	if ai_go == False:
		for item in room.chest:
			player.add_inventory(item)
			i = room.chest.index(item)
			del(room.chest[i])
		print(player.inventory)
		return True
	else:
		return False

#def next_room(ai_go = False):
#	if ai_go == False:




#these are the commands dictionaries
p_commands = {'attack' : attack, 'turtle' : turtle,
	'commands' : list_commands, 'heal' : heal,
	'see sword' : see_sword, 'grab item' : grab_item,
	'use item' : use_item, 'search chest' : search_chest}

g_commands = {'attack' : attack, 'turtle' : turtle,
	'heal' : heal}

commands = [p_commands, g_commands]