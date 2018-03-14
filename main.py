import self as self


class Inventory():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def list(self):
        print ("You are carrying:")
        for item in self.items:
            print (item.get_name())

    def get(self, type):
        items_of_type = []
        for item in self.items:
            if isinstance(item, type):
                items_of_type.append(item)
        return items_of_type

    def process_command(self, command):
        result = []
        for item in self.items:
            if item.get_name() in command:
                result.append(item.process_command(command))
        return result


class Item():
    def __init__(self, name):
        self.name = name
        self.known_commands = {}

    def get_name(self):
        return self.name

    def process_command(self, command):
        for a_command in self.known_commands:
            if a_command in command:
                self.known_commands[a_command](command)


class Literature(Item):
    def __init__(self, name, contents="This item is blank."):
        Item.__init__(self, name)
        self.contents = contents
        self.known_commands["read"] = self.read
        self.known_commands["write"] = self.write(command)

    def read(self, command):
        print (self.contents)

    def write(self, contents):
        self.contents = contents


class Room():
    def __init__(self, name, description, id):
        self.name = name
        self.description = description
        self.id = id
        self.items = []
        self.connectors = []
        self.rooms = {}

    def add_item(self, item):
        self.items.append(item)

    def add_room(self, direction, room):
        self.rooms[direction] = room

    def add_connection(self, room, connector, actions):
        for direction in actions:
            self.rooms[direction] = room
        self.connectors.append((connector, actions[0]))

    def enter_room(self, Inventory):
        print (self.name)
        print
        print (self.description)
        print
        for connector in self.connectors:
            print ("There is a " + connector[0] + \
                   " that goes " + connector[1] + ".")
        print
        for item in self.items:
            print ("You see a " + item.name + " here.")
        print

    def get_name(self):
        return self.name

    def is_valid_direction(self, direction):
        return direction in self.rooms.keys()

    def next_room(self, direction):
        return self.rooms[direction]

    def process_command(self, command, Inventory):
        if command in self.rooms.keys():
            new_room = self.next_room(command)
            return new_room
        elif "get" in command:
            for item in self.items:
                if item.name in command:
                    Inventory.add(item)
                    self.items.remove(item)
                    return "You picked up the " + item.name + "."
                else:
                    return "I don't know what you want to pick up."
        else:
            return None


class LightSource(Item):
    def __init__(self, name, on=False):
        self.on = on
        Item.__init__(self, name)
        self.known_commands["turn on"] = self.turn_on
        self.known_commands["turn off"] = self.turn_off

    @staticmethod
    def is_one_on(sources):
        if len(sources) > 0:
            for source in sources:
                if source.is_on():
                    return True
        return False

    def is_on(self):
        return self.on

    def turn_on(self, command):
        self.on = True
        print ("The " + self.name + " is on.")

    def turn_off(self, command):
        self.on = False
        print ("The " + self.name + " is off.")


class Flashlight(LightSource):
    def __init__(self, name="flashlight", battery_level=100, on=False):
        LightSource.__init__(self, name, on)
        self.battery_level = battery_level

    def change_batteries(self):
        self.battery_level = 100

    def compute_usage(self):
        # Compute the time it's been on and then drain the battery an equal amount
        pass



    class DarkRoom(Room):
        def enter_room(self, Inventory):
            light_sources = Inventory.get(LightSource)
            if LightSource.is_one_on(light_sources):
                Room.enter_room(self, Inventory)
            else:
                print ("A ghost came up from behind and possessed you.")
                print ("Game over.")
                exit()


lobby = Room ('You have reached Coronado Hotel, Welcome', 'You are in the lobby', 'l')
frontdesk = Room('Front Desk', 'You reached the front desk, there is no one here ', 'f')
patio = Room('Patio', 'You are in the patio, smoking is allowed.', 'p')
elevator = Room('Elevator', 'You attempt to take the elevator but you need an elevator pass', 'e')
openbar = Room('Open Bar', 'You reached the open bar, there is a man lying on the floor', 'o')
cafe = Room('Cafe', 'You are in the Cafe, there is a cash register to your right', 'c')
parkinglot = Room('Parking Lot', 'You are in the parking lot, there is a car in the distance', 'pl')
entrance = Room('Entrance', 'You reached the entrance of the hotel, you try to open it but its locked','ent')






frontdesk.add_connection(lobby, "passage", ["south", "s"])
lobby.add_connection(frontdesk, "passage", ["north", "n"])

lobby.add_connection(patio, "hallway", ["west", "w"])
patio.add_connection(lobby, "hallway", ["east", "e"])

lobby.add_connection(elevator, "elevator", ["east", "e"])
elevator.add_connection(lobby, "passage", ["west", "w"])

patio.add_connection(openbar, "passage", ["north", "n"])
patio.add_connection(cafe, "path", ["south", "s"])

openbar.add_connection(patio, "passage", ["south", "w"])
cafe.add_connection(patio, "path", ["north", "n"])

cafe.add_connection(parkinglot, "passage", ["east", "e"])
parkinglot.add_connection(cafe, "passage", ["west", "w"])

parkinglot.add_connection(entrance, "passage", ["south", "s"])
entrance.add_connection(parkinglot, "passage", ["north", "n"])




# kitchen.add_room('North', dining)

# dining.add_room('South', kitchen)

# dining.add_room('North', hallway)

# hallway.add_room('South', dining)

# hallway.add_room('East', living)

inventory = Inventory()
current_room = lobby
current_room.enter_room(inventory)
frontdesk.add_item(Flashlight())



while True:
    command = raw_input("What do you want to do?")
    if command in ["exit","x", "quit", "q"]:
        break

    result = current_room.process_command(command, inventory)
    if isinstance(result, Room):
        current_room = result
        result.enter_room(inventory)
        continue
    elif isinstance(result, str):
        print result
        continue

    else:
        print "I don't know what you mean"


