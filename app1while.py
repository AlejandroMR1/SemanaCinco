def eliminar_duplicados(lista):

    conjunto = set(lista)

    lista_sin_duplicados = list(conjunto)
    return lista_sin_duplicados

numeros = [1, 2, 2, 3, 4, 4, 5]
resultado = eliminar_duplicados(numeros)
print(resultado)  