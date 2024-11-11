print("EJERCICIO Nº1")
""""
DATOS DE CURSOS  EN HORAS
MINIMO   => 2.5
PROMEDIO => 4
MAXIMO   => 7 
CURSO DALTO => 1.5

2.5 = 100
1.5 = ?
1 = 0.025


A) DIFERENCIAS PORCENTUALES
1. Diferencia en porcentaje entre el curso 
actual y el mas rapido de otros cursos
1. Diferencia en porcentaje  entre el curso 
actual y el mas lento de otros cursos
1. Diferencia en porcentaje  entre el curso 
actual y el promedio de los cursos

B) PORCENTAJES DE MATERIAL INSERVIBLE QUE SE REDUCEN EN
DATOS: 
Crudo otros cursos : 5 
Crudo curso dalto = 3.5
- el promedio de los cursos 
- el curso actual 

C) Ver 10 horas de este curso es aquivalente a ver cuantas horas de otros
cursos. Y al reves
"""

# variables
curso_min = 2.5
curso_promedio = 4
curso_maximo = 7
curso_dalto = 1.5
# variables de crudo
crudo_otro_curso = 5
crudo_otro_dalto= 3.5

#  diferencias de duracion 
diferencia_porcentual_min = 100 - curso_dalto / curso_min * 100
diferencia_porcentual_max = 100 - curso_dalto / curso_maximo * 100
diferencia_porcentual_promedio =100 - curso_dalto / curso_promedio * 100
# calculando el promedio de tiempo vacio 
tiempo_vacio_promedio = 100 - curso_promedio * 1000 // crudo_otro_curso / 10 # => 20

# mostrando los resultados
print(f"Diferencia porcentual con el curso max: {diferencia_porcentual_max}")
print(f"Diferencia porcentual con el curso min: {diferencia_porcentual_min}")
print(f"Diferencia porcentual con el curso promedio: {diferencia_porcentual_promedio}")
# mostrando resultado del material inservible 
print(f"Un curso elimina un {tiempo_vacio_promedio}% de tiempo vacio.")
