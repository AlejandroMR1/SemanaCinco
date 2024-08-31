def buscar_palabra(diccionario, palabra):
    definicion = diccionario.get(palabra)
    
    if definicion:
        return f"Definición de '{palabra}': {definicion}"
    else:
        return f"La palabra '{palabra}' no se encontró en el diccionario."

diccionario_palabras = {
    'hogar': 'Lugar donde permanece una persona en comodidad.',
    'computadora': 'Dispositivo electrónico para procesar datos.',
    'libro': 'Conjunto de hojas encuadernadas que contienen texto o imágenes.'
}

palabra_a_buscar = 'libro'
resultado = buscar_palabra(diccionario_palabras, palabra_a_buscar)
print(resultado)

palabra_a_buscar = 'ladron'
resultado = buscar_palabra(diccionario_palabras, palabra_a_buscar)
print(resultado)