class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def printcoord(self):
        print(f"({self.x}, {self.y})")

    def printxy(self):
        print(f"x = {self.x}, y = {self.y}")
    
    def changexy(self):
        self.x = int(input("x = "))
        self.y = int(input("y = "))
        print(f"({self.x}, {self.y})")

point = Point(1, 2)
point.printcoord()
point.printxy()
point.changexy()