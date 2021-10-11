class Player:
    def __init__(self):
        self.name = ""
        self.inventory = []
    def set_name(self, name):
        self.name = name
    def add_inventory(self, item):
        self.inventory += items
 
class Room:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.items = []
    def set_name(self, name):
        self.name = name
    def add_items(self, items):
        self.items += items
    def remove_item(self, item):
        self.items.remove(item)
    def set_description(self, description):
        self.description = description
 
# Print title screen
print ("+---------------------------------------+")
print ("| Text Adventure Game |")
print ("+---------------------------------------+")
print ()
 
# Build player
player = Player()
input = input("Please enter your name: ")
player.set_name(input)
print ("Hello, " + player.name + ".\n")
 
# Build rooms, room items, and map
map_width, map_height = 2, 2
rooms = [[Room() for x in range(map_width)] for y in range(map_height)]
rooms[0][0].set_name("Bedroom")
rooms[0][0].set_description("You are in your bedroom.")
rooms[0][0].add_items(["wallet", "keys"])
rooms[0][1].set_name("Bathroom")
rooms[0][1].set_description("You are in the bathroom.")
rooms[0][1].add_items(["toilet paper", "magazine"])
rooms[1][0].set_name("Kitchen")
rooms[1][0].set_description("You are in the kitchen.")
rooms[1][0].add_items(["towel", "chainsaw"])
rooms[1][1].set_name("Garage")
rooms[1][1].set_description("You are in the garage.")
rooms[1][1].add_items(["car", "gasoline"])
 
def move(input, rooms, x, y):
    if input == "n":
        if y > 0: y -= 1
        else: print ("You can't go that way.")
    elif input == "s":
        if y < map_height - 1: y += 1
        else: print ("You can't go that way.")
    elif input == "e":
        if x > 0: x -= 1
        else: print ("You can't go that way.")
    elif input == "w":
        if x < map_width - 1: x += 1
        else: print ("You can't go that way.")
    return x, y
 
def get(inventory, item, room):
    if item in room.items:
        inventory.append(item)
        room.remove_item(item)
        print ("You pick up the " + item + ".")
    else:
        print ("You don't see that here.")
 
x, y = 0, 0
print (rooms[x][y].name + ": " + rooms[x][y].description)
print ("You see: " + str(rooms[x][y].items))
playing = True
while (playing):
    input_move = input("> ")
    if (input == "n" or input == "s" or input == "e" or input == "w"):
        x, y = move(input_move, rooms, x, y)
        print (rooms[x][y].name + ": " + rooms[x][y].description)
        print ("You see: " + str(rooms[x][y].items))
    elif input_move == "look":
        print (rooms[x][y].name + ": " + rooms[x][y].description)
        print ("You see: " + str(rooms[x][y].items))
    elif input_move[:4] == "get ":
        item = input[4:]
        get(player.inventory, item, rooms[x][y])
    elif input_move == "i":
        print ("Inventory: " + str(player.inventory))
    elif input_move == "help":
        print ("Type n/e/s/w to move your player")
        print ("Type i to view your inventory")
        print ("Type quit to quit the game")
        print ("Other commands: get, look, open, close, and more.")
    elif input_move == "quit":
        playing = False
    else: print ("I don't understand.")