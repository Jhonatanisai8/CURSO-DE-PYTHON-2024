
print("Iterando conjuntos")
# puede ser una conjunto
animales = {"gato","perro","loro","cocodrilo"}
numeros = {12,34,56,78}

# iteramos la conjunto 
for animal in animales:
    print(f"Ahpra la variable es igual a: {animal}")
    
# multiplicando los elementos de un conjunto y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10 
    print(f"resultado {numero} x 10: {resultado}")
    
# iterando sobre conjuntos del mismo tamaño al mismo tamaño 
for numero,animal in zip(animales,numeros):
    print(f"recorriendo conjunto 1: {animal}")
    print(f"recorriendo conjunto 2: {numero}")

# for con inicio y fin 
for num in range(5,10): #5 al 9
    print(f"iteracion {num}")
print("")

# for con fin 
for n in range(5): # de 0 a 4
    print(f"iteracion {n}")

# forma correcta de iterar una conjunto
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"indice {indice}, valor {valor}")
    
# usando el else el bucle for 
print("usando el for-else")
for numero in numeros:
    print(f"ejecutando {numero}")
else:
    print("el bucle termino")
    
    