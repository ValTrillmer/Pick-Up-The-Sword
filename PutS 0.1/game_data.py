descriptors = {"sharp" : 4,
"furry" : 1,
"rusty" : 3,
"snakes" : 2,
"gleaming" : 5
}

names = "thwacker poop bully whimpy destructor crumble notverygood".split()


#creature format
#name, hp, dfs, atk, alive, inventory, a_inventory, cmd
#string, int, int, int, Bool, [], [], {}
creatures = [
	["You", 20, 4, 2, True, [], [], None],
	["ghoul", 25, 5, 2, True, [], [], None],
	["ghoul chief", 50, 10, 5, True, [], [], None],
	["ghoul king", 100, 10, 10, True, [], [], None]
]

rooms = [
	["dining room", [], [], []],
	["store room", [], [], []],
	["kitchen", [], [], []],
	["throne room", [], [], []],
]