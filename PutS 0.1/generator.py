import random
from room import room
from character import character
from game_data import descriptors, names, creatures, rooms
from sword import sword
from item import item

def fill_chest(room):
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
			room.chest.append(item)
			y = y + 1
		else:
			empty = False


#dungeon generators
def create_enemy():
	x = random.randint(1, len(creatures) - 1)
	npc = character(creatures[x][0], creatures[x][1], creatures[x][2], creatures[x][3], creatures[x][4], creatures[x][5], creatures[x][6], creatures[x][7])
	npc.set_commands()
	return npc

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
	p.set_commands()
	return p

def create_room():
	x = random.randint(0, len(rooms) - 2)
	r  = room(rooms[x][0], rooms[x][1], rooms[x][2], rooms[x][3])
	y = create_enemy()
	r.entity.append(y)
	return room

def create_dungeon():
	x = random.randint(2, 4)
	dungeon = []
	while len(dungeon) < x:
		y = create_room()
		dungeon.append(y)
	return dungeon


#this is the game
def create_game():
	player = create_player()
	x = create_sword()
	player.equip_sword(x)
	dungeon = create_dungeon()
	dungeon[0].entity.append(player)