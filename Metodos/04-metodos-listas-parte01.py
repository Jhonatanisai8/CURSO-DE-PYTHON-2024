print("METODOS DE LISTAS EN PYTHON")

# CREAMOS LA LISTA 
lista_numeros = list([1,2,3,4])
print(f"Lista inicial: {lista_numeros}")

# append(x): Agrega un elemento x al final de la lista.
lista_numeros.append(4)
# mostramos la lista actualizada para ver los cambios
print(f"Lista actualizada: {lista_numeros}")

# extend(iterable): Extiende la lista agregando todos los 
# elementos de un iterable (como otra lista).
lista_numeros.extend([5,6,7])
print(f"Lista actualizada: {lista_numeros}")

# insert(i, x): Inserta un elemento x en la posición i.
lista_numeros.insert(3,10)
print(f"Lista actualizada: {lista_numeros}")

# remove(x): Elimina el primer elemento con el valor x. Da error si no existe.
lista_numeros.remove(3)
print(f"Lista actualizada: {lista_numeros}")

# pop(i): Elimina y devuelve el elemento en la posición i. Si i no se
# especifica, elimina el último elemento.
lista_numeros.pop(0)
print(f"Lista actualizada: {lista_numeros}")


# index(x, start, end): Devuelve el índice de la primera aparición de x entre las posiciones
indice = lista_numeros.index(4)
print(f"indice: {indice}")

# count(x): Devuelve el número de veces que x aparece en la lista.
veces_aparecido = lista_numeros.count(4)
print(f"Veces: {veces_aparecido}")

"""sort(reverse=False): Ordena los elementos de la lista en orden ascendente. 
Usa reverse=True para ordenar en orden descendente."""
lista_numeros.sort()
print(f"Lista actualizada: {lista_numeros}")
lista_numeros.sort(reverse=True)
print(f"Lista actualizada: {lista_numeros}")

# reverse(): Invierte el orden de los elementos en la lista
lista_numeros.reverse()
print(f"Lista reverse: {lista_numeros}")

# copy(): Devuelve una copia superficial de la lista. Esto es útil para crear una lista idéntica sin vincularla a la original.
lista_copia = lista_numeros.copy()
print(f"Lista nueva: {lista_copia}")
# clear(): Elimina todos los elementos de la lista, dejándola vacía.
lista_numeros.clear()
print(f"Lista actualizada: {lista_numeros}")

