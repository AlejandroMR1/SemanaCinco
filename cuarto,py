def agregar_palabras():
    diccionario = {}
    
    while True:
        palabra = input("Ingresa una palabra : ").strip()
 
        definicion = input(f"Ingresa la definición para '{palabra}': ").strip()
        diccionario[palabra] = definicion

        op = input("Quiere ingresar otra palabra?: ")
        
        if op.lower() != 'si':
            break
        
    return diccionario

def mostrar_diccionario(diccionario):
    if diccionario:
        print("\nDiccionario de palabras y definiciones:")
        for palabra, definicion in diccionario.items():
            print(f"{palabra}: {definicion}")
    else:
        print("El diccionario está vacío.")

diccionario_palabras = agregar_palabras()
mostrar_diccionario(diccionario_palabras)
