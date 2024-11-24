print("BUCLES FLOR EN PYTHON")

for i in range(5):
    print("Hola ",i)

#Ejemplo 1: Iterar sobre una lista
print("RECORRIENDO UNA LISTA")
lista_animales = list(["Perro","Gato","Caballo","Conejo"])
for lista_animales in lista_animales:
    print(lista_animales)

# Ejemplo 2: Usando range() para un rango de números
print("RECORRIENDO LOS NUMEROS")
for i in range(5):
    print(i)

# Puedes especificar un rango con inicio, fin y paso:
print("RECORRIENDO DE 2 O EN 2")
for i in range(1, 10, 2):  # Del 1 al 9, con paso de 2
    print(i)

# Ejemplo 3: Iterar sobre una cadena
print("recorriendo una cadena".upper())
cadena = "cocodrilo"
for cadena in cadena:
    print(cadena)

# Ejemplo 4: for con índice (usando enumerate)
print("usando 'enumerate'".upper())
lista_frutas = ["mango","limon","cereza","platano","papaya"]
for indice,lista_frutas in enumerate(lista_frutas):
    print(f"indice: {indice}, fruta: {lista_frutas}")

# Ejemplo 5: Salir del bucle con break
print("recorriendo numeros pero usando 'break'".upper())
for i in range(20):
    if i == 5:
        print("encontre el numero 5, saliendo del bucle")
        break
    print(i)

# Ejemplo 6: Saltar una iteración con continue
print("recorriendo numero usando continue".upper())
for numero in range (5):
    if numero == 4: #salta el numero 4
        continue
    print(numero)
    
# ejemplo 7: iterando dos listas 
print("reccoriendo dos listas al mismo tiempo.".upper())
lista_paises = ["Colombia","Peru","Brazil","Argentina","Paraguay","Venezuela","Chile"]
lista_numeros = [22,44,33,88,77,99,100]
for lista_paises,lista_numeros in zip(lista_paises,lista_numeros):
    print(f"Recorriendo lista 1: {lista_paises}")
    print(f"Recorriendo lista 2: {lista_numeros}")

# ejemplo 8: for desde un inicio y un final 
print("for desde un incio y un final ".upper())
for numero in range (5,10):
    print(numero)

# ejemplo 9: iterando una lista  de una forma no optima
print("forma no optima de recorrer una lista".upper())  
lista_vegatales = ["zanahoria","papa","camote"]
for i in range(len(lista_vegatales)):
    print(lista_vegatales[i])

# ejemplo 10: iterando una lista  de una forma no optima
print("forma  optima de recorrer una lista".upper())  
lista_vegatales = ["zanahoria","papa","camote"]
for i in enumerate(lista_vegatales):
    ind = i[0]
    valor = i[1]
    print(f"indice: {ind}, valor: {valor}")
    
# ejemplo 10: for usando else
list_num = [3,6,5,2,4]
for numero in list_num:
    print(f"ejecutando el ultimo bucle, valor actual {numero}")
else:
    print("el bucle finalizo")