import random

descriptors = 'funny sharp dull snakes powerful gleeming wobbly ugly golden rakish silver furry yucky slimy smelly rusty mysterious'.split()
names = "thwacker poop bully whimpy destructor crumble notverygood".split()
swords = []

class sword:
	def __init__(self, name, blade, hilt, magic):
		self.name = name
		self.blade = blade
		self.hilt = hilt
		self.magic = magic

	def __repr__(self):
		return self.name

def get_descriptor():
	descriptor_index = random.randint(0, len(descriptors) - 1)
	return descriptors[descriptor_index]

def get_name():
	name_index = random.randint(0, len(names) - 1)
	return names[name_index]

def apply_descriptor():

	new_sword = sword(get_name(), get_descriptor(), get_descriptor(), get_descriptor())
	print("You pick up the sword. It's name is " + new_sword.name + ". It's blade is " + new_sword.blade + 
		". It's hilt is " + new_sword.hilt + ". It's magic is " + new_sword.magic + ".")
	return new_sword

running  = True

while running:
	print("You see a sword. Do you pick it up?")
	choice = input("> ")
	if choice == "y":
		new_sword = apply_descriptor()
		print("do you want to keep the sword?")
		choice = input("> ")
		if choice == "y":
		 	swords.append(new_sword)
		 	print(swords)
		elif choice == "n":
			print("You are no adventurer")
			running = False
		else:
			print("y or n")
	elif choice == "n":
		print("You are no adventurer")
		running = False
	else:
		print("y or n")