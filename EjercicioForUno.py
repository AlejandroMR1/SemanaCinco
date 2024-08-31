def suma_elementos (lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma
    
numeros = [1,3,2,4,5,7]
resultado = suma_elementos(numeros)
print(f"La suma total de los número es: {resultado}")