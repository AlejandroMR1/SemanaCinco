def contar_pares(lista):
    conteo = 0
    for numero in lista:
        if numero % 2 == 0:
            conteo += 1
    return conteo

numeros = [1, 2, 5, 7, 8, 10]
resultado = contar_pares(numeros)
print(f"La cantidad de números pares es: {resultado}")