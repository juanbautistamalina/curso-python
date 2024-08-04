 # Promedio de duraciones
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_actual = 1.5

# Duración de crudos
crudo_promedio = 5
crudo_actual = 3.5




# Diferencias de duración (EJERCICIO A)
diferencias_con_min = 100 -  (curso_actual/otros_cursos_min * 100)
print(f"El curso actual dura un {diferencias_con_min}% menos que el más rápido")

diferencias_con_max = 100 -  (curso_actual * 1000 //otros_cursos_max / 10)
print(f"El curso actual dura un {diferencias_con_max}% menos que el más largo")

diferencias_con_promedio = 100 -  (curso_actual/otros_cursos_promedio * 100)
print(f"El curso actual dura un {diferencias_con_promedio}% menos que el promedio")


# Mostrando la cantidad de espacios vacíos que se remueven  (EJERCICIO B)
tiempo_vacio_promedio = 100 -  (otros_cursos_promedio * 1000 //crudo_promedio / 10)
tiempo_vacio_actual = 100 -  (curso_actual * 1000 //crudo_actual / 10)

print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío")
print(f"Este curso eiminó un {tiempo_vacio_actual}% de tiempo vacío")

# Mostrando diferencias si los cursos duraran 10 horas (EJERCICIO C)
print(f"Ver 10 horas de este curso, equivale a ver {otros_cursos_promedio * 100 //curso_actual/10} horas de otros cursos")
print(f"Ver 10 horas de otros cursos, equivale a ver {curso_actual * 100 //otros_cursos_promedio/10} horas de el curso actual")