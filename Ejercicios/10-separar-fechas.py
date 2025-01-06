"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento 
en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
Adaptar el programa anterior para que también funcione cuando el día 
o el mes se introduzcan con un solo carácter.
"""

def mostrar_fecha(fecha):
    dia, mes, año = fecha.split('/')
    print(f"Día: {dia}, Mes: {mes}, Año: {año}")
    
mostrar_fecha("12/01/1232")