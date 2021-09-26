class Fizzbuzz:
    def __init__(self):
        self.nombre = float(input("Quel est ton chiffre : "))
        self.fizzbuzz(15, self.nombre, "fizzbuzz")
        self.fizzbuzz(3, self.nombre, "fizz")
        self.fizzbuzz(5, self.nombre, "buzz")
        
    def fizzbuzz(self, multiple, nombre, affiche):
        if nombre%multiple == 0:
            print(affiche)
            exit()
        else:
            return
Fizzbuzz()
