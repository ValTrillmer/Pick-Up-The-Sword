import random

def heal(x, y, ai_go = False):
	l = random.randint(x, y)
	if ai_go == False:
		print("You gain " + str(l) + " life!")
		player.hp = player.hp + l
		return False
	else:
		print("Your opponent gained " + str(l) + " life!")
		#room.enemy[0].hp = room.enemy[0].hp + l
		return True

item_func = {
	["potion", heal(5, 8, ai_go), False]
}