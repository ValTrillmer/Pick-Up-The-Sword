import sys
import random

party = []
corpses = []
given_names = ["Chet", "Burt", "Nard", "Will", "Preibus", "Carlchuck"]
surnames = ["Butterball", "Butterworth", "Butterly", "Buttersson"]
exp_to_lvl = {2 : 5, 3 : 10, 4 : 20}

class person:
	def __init__(self, name, hp, actions, level, exp, exp_total, exp_given):
		self.name = name
		self.hp = hp
		self.actions = actions
		self.level = level
		self.exp = exp
		self.exp_total = exp_total
		self.exp_given = exp_given

	def __repr__(self):
		return self.name

	def single_attack(self):
		target = selecttarget(self)
		dmg = self.level * random.randint(1,10)
		target.hp = target.hp - dmg
		print(self.name + " attacks " + target.name + " for " + str(dmg) + " damage! And is gay!")
		print(target.name + " has " + str(target.hp) + " hp left.")

	def group_attack(self):
		y = all_target(self)
		dmg = self.level * random.randint(1,2)
		print(self.name + " attacks everyone for " + str(dmg) + " damage! And is gay!")
		for z in y:
			z.hp = z.hp - dmg
			print(z.name + " has " + str(z.hp) + " hp left.")

def selecttarget(x):
	selected = False
	while not selected:
		target = party[random.randint(0,len(party)-1)]
		if target != x:
			selected = True
	return target

def all_target(x):
	y = list(party)
	y.remove(x)
	return y

def create_party():
	full_party = False
	while not full_party:
		x = create_character()
		party.append(x)
		print(x)
		if len(party) < 5:
			full_party = False
		else:
			full_party = True
	print(party)

def create_character():
	y = random.randint(0,len(given_names)-1)
	z = random.randint(0,len(surnames)-1)
	x = person(given_names[y] + " " + surnames[z], random.randint(10, 20), [], 1, 0, 0, 5)
	x.actions.append(x.single_attack)
	x.actions.append(x.group_attack)
	return x

def kill_check(x):
	for c in party:
		if c.hp <= 0:
			party.remove(c)
			corpses.append(c)
			print(str(corpses) + " are dead")
			x.exp = x.exp + c.exp_given
			x.exp_total = x.exp_total + c.exp_given
		else:
			pass

def level_check(x):
	if x.exp >= exp_to_lvl[x.level + 1]:
		x.level = x.level + 1
		x.exp = x.exp - exp_to_lvl[x.level]
		print(x.name + " has reached level " + str(x.level) + "!")


create_party()

running = True
while running:
	for x in party:
		i = random.randint(0,len(x.actions)-1)
		x.actions[i]()
		kill_check(x)
		level_check(x)
		print(party)
		if len(party) == 1:
			print(x.exp_total)
			print(sys.version)
			running = False