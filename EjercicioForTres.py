def elemento_mas_grande(lista):
    
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
    return maximo

numeros = [3, 7, 1, 4, 9, 8]
resultado = elemento_mas_grande(numeros)
print(f"El elemento más grande de la lista es: {resultado}")