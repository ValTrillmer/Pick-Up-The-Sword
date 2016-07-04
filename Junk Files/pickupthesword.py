import random, pickle, os

descriptors = 'funny sharp dull snakes powerful gleeming wobbly ugly golden rakish silver furry yucky slimy smelly rusty mysterious'.split()
names = "thwacker poop bully whimpy destructor crumble notverygood".split()
saves = []
swords = []

class sword:
	def __init__(self, name, blade, hilt, magic):
		self.name = name
		self.blade = blade
		self.hilt = hilt
		self.magic = magic

	def __repr__(self):
		return self.name

	def view(self):
		print("This is " + self.name + ". Its blade is " + self.blade + ". Its hilt is " + self.hilt + ". Its magic is " + self.magic + ".")

def save_file():
	running = True
	while running:
		print("1. New Save File\n2. Overwrite Save File")
		choice = input("> ")
		if choice == "1":
			file_name = input("> ") + ".p"
			with open(file_name, "wb") as f:
				pickle.dump(swords, f)
			saves.append(file_name)
			running = False
		elif choice == "2":
			print(str(saves) + "\nWhich file do you want to overwrite?")
			overwrite = input("> ") + ".p"
			for file in saves:
				if overwrite == file:
					with open(overwrite, "wb") as f:
						pickle.dump(saves, f)
					running = False
				else:
					running = False
		else:
			print("try again")

def open_save(file_name):
	test = os.stat(file_name)
	if test.st_size != 0:
		with open(file_name, 'rb') as f:
			s = pickle.load(f)
		return s	
	else:
		swords = []

def get_descriptor():
	descriptor_index = random.randint(0, len(descriptors) - 1)
	return descriptors[descriptor_index]

def get_name():
	name_index = random.randint(0, len(names) - 1)
	return names[name_index]

def apply_descriptor():

	new_sword = sword(get_name(), get_descriptor(), get_descriptor(), get_descriptor())
	print("You pick up the sword. Its name is " + new_sword.name + ". Its blade is " + new_sword.blade + 
		". Its hilt is " + new_sword.hilt + ". Its magic is " + new_sword.magic + ".")
	return new_sword

def pick_sword():
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
			 	print("save the game?")
			 	choice2 = input("> ")
			 	if choice2 == "y":
			 		save_file()
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

def load_game():
	print("Which save file?\n" + str(saves))
	choice = input("> ") + ".p"
	print(choice)
	for save in saves:
		if choice == save:
			swords = open_save(choice)
			print(swords)
			pick_sword()

def list_files():
	# returns a list of names (with extension, without full path) of all files 
	# in folder path
	files = []
	for name in os.listdir("."):
		if os.path.isfile(os.path.join(".", name)):
			if name.endswith(".p"):
				files.append(name)
	return files

saves = list_files()

running = True
while running:
	print("Welcome to Pick Up The Sword \n\n1. New Game\n2. Load Game\n3. Quit")
	choice = input("> ")
	if choice == "1":
		pick_sword()
	elif choice == "2":
		load_game()
	elif choice == "3":
		running = False
	else:
		print("try again")