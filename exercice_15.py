def fizzbuzz(nombre):
    if nombre%15 == 0:
        result = "fizzbuzz"
        return result
    elif nombre%3 == 0:
        result = "fizz"
        return result
    elif nombre%5 == 0:
        result =  "buzz"
        return result
    else:
        return
Nombre = float(input("Quel est ton chiffre : "))
print(fizzbuzz(Nombre))