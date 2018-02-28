class Inventory():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def list(self):
        print "you are carrying:"
        for item in self.items:
            print item.getname()


class Item():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Literature(Item):
    def __init__(self, name, contents= "This item is blank"):
        Item.__init__(self, name)
        self.contents = contents

    def read(selfself):
        print self.contents

    def write(selfself,contents):
        self.contents = contents

class Flashlight(Item):
    def __init__(self, name, Battery_leveel=100, state="off"):
        item.__init__(self, name)
        self.battery_level + battery_level
        self.state = state

    def turn_on(self):
        self.state= "On"

    def turn_off(self):
        self.state = "Off"

    def change_batteries(self):
        self.battery_level=100

    def compute_usage(self):
        # compute the time it's been on and then drain the battery an equal amount
        pass
