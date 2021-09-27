# petit 1 #
def f(x):
    fx=3*x+2
    return fx
print(f(4))

# petit 2 #
def g(x):
    g= x**2 - 3*x+2
    return g
print(g(4))

# petit 3 a #
def degres_fahrenheit(degres):
    convertion_cels = 5/9 *(degres - 32)
    return convertion_cels
print(degres_fahrenheit(10))

# petit 3 b #
def degres_celsius(degres):
    convertion_fahr = (degres * 9/5) + 32
    return convertion_fahr
print(degres_celsius(18))

