def promedio_notas(alumnos):
    total_notas = 0
    cantidad_notas = 0
    
    for i in alumnos.values():
        total_notas += i
        cantidad_notas += 1
    
    if cantidad_notas == 0:  
        return 0
    
    promedio = total_notas / cantidad_notas
    return promedio

# Ejemplo de uso
alumnos = {'Victor': 120, 'Karla': 50, 'Gabriel': 70, 'Alejo': 2}
promedio = promedio_notas(alumnos)
print("El promedio de las notas es:", promedio)