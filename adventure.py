from room import Room

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


# inventory = Inventory()
current_room = lobby
current_room.enter_room()



while True:
    command = raw_input("What direction do you want to go?")
    if command in ["exit","x", "quit", "q"]:
        break

    result = current_room.process_command(command,None)
    if isinstance(result, Room):
        current_room = result
        result.enter_room()
        continue
    elif isinstance(result, str):
        print result
        continue

    else:
        print "I don't know what you mean"


    direction = raw_input("What direction do you want to go")
    if direction == 'x':
        break
    elif current_room.is_valid_direction(direction):
         current_room = current_room.next_room(direction)
         current_room.enter_room()
    else:
        print "Ouch! You ran into a wall."
