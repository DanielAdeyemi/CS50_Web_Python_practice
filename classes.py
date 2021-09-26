class Point():
    def __init__(self, x, y):  # create an object, self references object itself
        self.x = x
        self.y = y


p = Point(2, 8)  # initiate new Point and print the data from inside
print(p.x)
print(p.y)


class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    def add_passanger(self, name):
        if not self.open_seats():
            return False
        self.passangers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passangers)


flight = Flight(3)
people = ["Harry", "Ron", "Hermione", "Ginny"]

for name in people:
    if flight.add_passanger(name):
        print(f"{name} was added to flight")
    else:
        print(f"Sorry, {name}! No seats available for this flight")
