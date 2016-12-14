import random

#these are my commands

#receives input to determine which object to apply the damage toward
def turtle(ai_go = False):
	#player's turn
	if ai_go == False:
		print("You have turtled")
		return False
	#game turn
	else:
		print("Your opponent has turtled")
		return True