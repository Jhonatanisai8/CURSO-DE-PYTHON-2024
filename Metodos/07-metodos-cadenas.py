# Convierte todos los caracteres de la cadena a mayúsculas.
cadena = "hola"
print(cadena.upper())
# Convierte todos los caracteres a minúsculas
fruta = "LIMON"
print(fruta.lower())
# Convierte la primera letra en mayúscula y el resto en minúsculas.
saludo ="hola como estas?"
print(saludo.capitalize())
# Convierte la primera letra de cada palabra en mayúscula.
frase = "hola mundo"
print(frase.title())
# Elimina espacios (u otros caracteres especificados) al inicio y al final de la cadena.
pais = " Holanda "
print(pais.strip())
# Elimina espacios al inicio de la cadena.
animal = " perro"
print(animal.lstrip())
# Elimina espacios al final de la cadena.
nombre = "paulo "
print(nombre.rstrip())
# Devuelve el índice de la primera aparición de sub. Si no se encuentra, devuelve -1.
mi_frase = "hola mundo"
print(mi_frase.find("mundo")) 
# Reemplaza todas las ocurrencias de old por new.
mi_saludo = "hola mundo"
print(mi_saludo.replace("mundo","python"))
# Cuenta cuántas veces aparece sub en la cadena.
hola = "hola como estas, hola"
print(hola.count("hola"))
# Devuelve True si todos los caracteres son números.
numeros = "123456"
print(numeros.isdigit())
# Devuelve True si todos los caracteres son letras o números.
letras_numeros = "123adf"
print(letras_numeros.isalnum())








