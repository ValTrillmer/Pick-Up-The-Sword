import random

descriptors = 'funny sharp dull snakes powerful gleeming wobbly ugly golden rakish silver furry yucky slimy smelly rusty mysterious'.split()


class sword:
	def __init__(self, blade, hilt, magic):
		self.blade = blade
		self.hilt = hilt
		self.magic = magic

def get_descriptor():
	descriptor_index = random.randint(0, len(descriptors) - 1)
	return descriptors[descriptor_index]

def apply_descriptor():
	blade = get_descriptor()
	hilt = get_descriptor()
	magic = get_descriptor()

	new_sword = sword(blade, hilt, magic)
	print("You pick up the sword. It's blade is " + new_sword.blade + ". It's hilt is " + new_sword.hilt + ". It's magic is " + new_sword.magic + ".")

running  = True

while running:
	print("You see a sword. Do you pick it up?")
	choice = input("> ")
	if choice == "y":
		apply_descriptor()
		running = False
	elif choice == "n":
		print("You are no adventurer")
		running = False
	else:
		print("y or n")