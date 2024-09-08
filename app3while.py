def contar_vocales(frase):
    # Definir las vocales
    vocales = "aeiouAEIOU"
    contador_vocales = 0
    index = 0
    
    # Convertir la frase a una lista de caracteres para usar el bucle while
    frase_lista = list(frase)
    
    # Recorre la frase con un bucle while
    while index < len(frase_lista):
        if frase_lista[index] in vocales:
            contador_vocales += 1
        index += 1
    
    return contador_vocales

# Solicitar al usuario que ingrese una frase
frase_usuario = input("Introduce una frase: ")
cantidad_vocales = contar_vocales(frase_usuario)

print(f"La cantidad de vocales en la frase es: {cantidad_vocales}")