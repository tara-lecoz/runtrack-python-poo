class Operation:
    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3

    def addition(self):
        add = (self.nombre1 + self.nombre2)
        print(add)

operation = Operation()
operation.addition()