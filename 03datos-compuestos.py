#dato compuesto
#creando una lista (se puede modificar)
lista = ["Mateo Diaz","Hola Mundo",12,True,4.6]

print("Primer elemento: ",lista[0])
print("Segundo elemento: ",lista[1])

print(lista)
#esto es válido
lista[1] = "Juan Pedro"
print(lista)

#tuplas
#creando una tupla (no se puede modificar)
tupla = ("Mateo Diaz","Hola Mundo",12,True,4.6,)

#esto no es válido
#tupla[0] = "Pedro David"
print("tupla: ",tupla)

#creando un conjunto (set) no se pueden repetir datos
#no se accede a elementos por su indice.
conjunto = {"Mateo Diaz","Hola Mundo",12,True,4.6}
print(conjunto)

print("")
#diccionario (dic) (la estructura es key : valor y separados por comas)
diccionario = {
    'nombre': "Mateo Alonso",
    'apellido': "Juarez Lopez",
    'esta_alegre': True,
    'escala' : 12.4,
    'dato_duplicado': "Mateo Alonso"
}

#por indice
print(diccionario['nombre'])
print(diccionario['escala'])
# al valor de escala le sumamos 4
print(diccionario['escala'] + 5)

print(diccionario)
