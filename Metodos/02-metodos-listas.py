
print("METODOS PARA MANIPULAR LISTAS")
# CREA UNA LISTA
lista = list(["Bienvenido","Jhonatan",12])
print(lista)

# CUENTA LA CANTIDAD DE ELEMENTOS QUE HAY EN UNA LISTA
resultado =  len(lista)
print(f"Tamaño de la lista: {resultado}")

# AGREGA UN ELEMENTO A LA LISTA
lista.append("Nuevo valor")
print(lista)

# agregando la lista en un indice especefico
lista.insert(2,"Mundo Nuevo")
lista.insert(3,"2024")

print(lista)
resultado =  len(lista)
print(f"Tamaño de la lista: {resultado}")

# agregando varios elementos
lista.extend([False,2323])
print(lista)

# ELIMINANDO UN ELEMENTO DE LA LISTA (POR SU INDICE)
lista.pop(3)
print(lista)
print(f"Tamaño de la lista: {len(lista)}")
# para eliminar el ultimo elemento de la lista 
lista.pop(-1)
print(lista)
print(f"Tamaño de la lista: {len(lista)}")

# REMOVIENDO UN ELEMENTO POR SU VALOR 
lista.remove(12)
print(lista)
print(f"Tamaño de la lista: {len(lista)}")

# ORDENANDO LOS ELEMENTOS 
lista_numeros = list([34,54,67,1,2,34,55,56,77,2])
lista_numeros.sort();
print(lista_numeros)
lista_numeros.sort(reverse=True);
print(lista_numeros)

# invertimos los elementos de una lista 
lista_numeros.reverse()
print(lista_numeros)

# VERIFICAR SI UN ELEMENTOS SE ENCUENTRA EN LA LISTA 
posicion = lista_numeros.index(1)
print("Posicion: ",posicion)
# ELIMINANDO TODOS LOS ELEMENTOS DE LA LISTA 
lista.clear();
print(print)
