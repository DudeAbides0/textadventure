class Room():
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id
        self.items = []
        self.rooms = {}

    def add_item(self,item):
        self.items.append(item)

    def add_room(self, direction, room):
        self.rooms[direction] = room

    def connect_rooms(self, direction, room):
        opposite_direction = {'north': 'south', 's': 'n', 'e': 'w','w':'e'}
        self.add_room(direction, room)
        room.add_room(opposite_direction[direction], self)

    def enter_room(self):
        print(self.name)
        print(self.description)
        print
        for direction in self.rooms.keys():
            print "To the " + direction + " is a "+ self.rooms[direction].get_name()

    def get_name(self):
        return self.name

    def is_valid_direction(self, direction):
        return direction in self.rooms.keys()

    def next_room(self, direction):
        return self.rooms[direction]

kitchen = Room('kitchen', 'You are in the kitchen ', 'k')
dining = Room ('You have reached Bankerside Bank, Welcome', 'You are in the dining room', 'd')
hallway = Room('Hallway', 'You are in the hallway', 'h')
hallway2 = Room('Upstairs hallway,', 'you are in the hallway', 'uh')
bedroom1 = Room ('Bedroom,', 'You are in a bedroom', 'b1')
bedroom2 = Room ('Bedroom,', 'You are in a bedroom', 'b2')
bedroom3 = Room ('Bedroom,', 'You are in a bedroom', 'b3')
living = Room('Living Room', 'Your are in the living room.', 'lr')

kitchen.connect_rooms('n', dining)

kitchen.add_room('North', dining)

dining.add_room('South', kitchen)

dining.add_room('North', hallway)

hallway.add_room('South', dining)

hallway.add_room('East', living)




current_room = dining
dining.enter_room()

while True:
    direction = raw_input("what direction do you want to go?")
    if direction == 'x':
        break
    elif current_room.is_valid_direction(direction):
        current_room = current_room.next_room(direction)
        current_room.enter_room()
    else:
        print "Ouch! You ran into a wall."
