def generar_numeros_pares():
    numeros_pares = []
    numero = 1  

    while numero <= 100:
        if numero % 2 == 0:  
            numeros_pares.append(numero)
        numero += 1  

    return numeros_pares

lista_pares = generar_numeros_pares()
print("Números pares entre 1 y 100:",lista_pares)