alumnos = {}

while True:
    
    nombre = input(f"Ingresa el nombre del alumno : ")

    nota = float(input(f"Ingresa la nota de {nombre}: "))

    alumnos[nombre] = nota
    
    op = input("Deseas agregar otro estudiante?: ")
    
    if op.lower() != "si":
        
        break

print("\nDiccionario de alumnos y sus notas:")
print(alumnos)