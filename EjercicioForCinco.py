def invertir_lista(lista):
    nueva_lista = []
    for i in range(len(lista) - 1, -1, -1):
        nueva_lista.append(lista[i])
    return nueva_lista

numeros = [8, 3, 4, 7, 9, 1]
resultado = invertir_lista(numeros)
print(f"La lista invertida es la siguiente: {resultado}")