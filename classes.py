class Point():
    def __init__(self, x, y):  # create an object, self references object itself
        self.x = x
        self.y = y


p = Point(2, 8)  # initiate new Point and print the data from inside
print(p.x)
print(p.y)
