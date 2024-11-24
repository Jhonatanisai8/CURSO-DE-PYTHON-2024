print("otras iteraciones")
frutas = ["banana","manzana","pera","mango","limon","durazno","zandia"]

# uso del continue
for fruta in frutas:
    if fruta == 'manzana':#manzana no lo muestra
        continue
    print(f"me voy a comer una: {fruta}")
    
    
# uso del break 
print("uso del break....")
for fruta in frutas:
    print(f"me voy a comer una: {fruta}")
    if fruta == 'pera':
        break #termina el bucle 
    
# iterando cadenas
print("iterar cadenas")
cadena = "jhoanatan"
for caracter in cadena:
    print(caracter)

caracter = 'A'
print(type(caracter))

numeros = [1,2,3,4]
print(numeros)
# for en una linea de codigo 
numeros_duplicados = [x**3 for x in numeros]
print(f"{numeros_duplicados}")