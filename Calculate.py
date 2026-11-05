def suma(a,b):
    return a + b
def resta(a,b):
    return a - b  
def mult(a,b):
    return a * b
def div(a,b):
    if b == 0:
        print ('No se puede ejecutar la operaciòn, divisor es 0')
    else:
        return a / b

def pot(a,b):
    return a ** b
def quart(a,b):
    return a ** 1/2, b ** 1/2

a = float (input('Ingrese número 1: '))
b = float (input('Ingrese número 2: '))

print(f'Suma es: {suma(a,b)}, Resta es: {resta(a,b)}, Multiplicación es: {mult(a,b)}, División es: {div(a,b)}, La potencia de número 1 elevado al número 2 es: {pot(a,b)}, Raìz cuadrada es: {quart(a,b)}')