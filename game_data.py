from commands import commands

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
creatures = {
	"player" : ["You", 20, 4, 2, True, [], [], commands[0]],
	"ghoul" : ["ghoul", 25, 5, 2, True, [], [], commands[1]],
	"ghoul chief" : ["ghoul chief", 50, 10, 5, [], [], commands[1]],
	"ghoul king" : ["ghoul king", 100, 10, 10, [], [], commands[1]],
}