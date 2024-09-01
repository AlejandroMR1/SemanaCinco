def multiplicar_elementos(lista):
    nueva_lista = []
    for numero in lista:
        nueva_lista.append(numero * 2)
    return nueva_lista

numeros = [3, 2, 9, 1, 0, 7]
resultado = multiplicar_elementos(numeros)
print(f"La nueva lista con los elementos multiplicados por 2 es: {resultado}")