def alumno_con_mejor_nota(alumnos):
    mejor_alumno = None
    mejor_nota = -1  

    for alumno, nota in alumnos.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = alumno

    return mejor_alumno

# Ejemplo de uso
alumnos = {'Alejo': 200, 'Victor': 492, 'Gabriel': 50, 'Karla': 104}
mejor_alumno = alumno_con_mejor_nota(alumnos)
print("El alumno con la mejor nota es:", mejor_alumno)