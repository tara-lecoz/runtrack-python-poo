class Animal:
    def __init__(self, name):
        self.name = name   
        self.age = int(input("age = "))
        print(f"L'age de l'animal est {self.age} ans.")

    def nommer(self):
        print(f"L'animal se nomme {self.name}.")

    def vieillir(self):
        self.age = self.age + 1
        print(f"L'age de l'animal est {self.age} ans.")
        
animal1 = Animal("test")
animal1.vieillir()
animal1.nommer()