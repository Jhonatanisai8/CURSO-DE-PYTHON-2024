
print("METODOS EN DE STRING EN PYTHON")

cadena_01 = "Hola Mundo"
cadena_02 = "hola Python"

# nos muestra los metodos

resultado = dir(cadena_02)
print("resultado = dir(cadena_02): ",resultado)

# convertir  a mayuscula
resultado = cadena_02.upper()
print("cadena_02.upper(): ",resultado)

# convertir  a minuscula
resultado = cadena_02.lower()
print("cadena_02.lower(): ",resultado)

# primera letra en mayuscula
resultado = cadena_02.capitalize()
print("cadena_02.capitalize(): ",resultado)

# encuentra la primera aparacion del valor especifocado, si no devuelve 1
busqueda_find = cadena_02.find("a")
print("cadena_02.find(Hola) :",busqueda_find)

# buscamos una cadena dentro de otra cadena
busqueda_index = cadena_01.index("a")
print("cadena_01.index(a): ",busqueda_index)

# si es numerico, devolvemos true, sino devolvemos false
cadena_03 = "12A34"
es_numerico = cadena_03.isnumeric()
print("cadena_01.isnumeric(): ",es_numerico)

# si es alfanumerico, devolvemos true, ai no delvolvemos false
cadena_04 = "ABC "
es_alfanumerico = cadena_04.isalpha()
print("cadena_04.isalpha(): ",es_alfanumerico)

# buscamos una cadena en otra cadena. devuelve el numero que veces que aparece
ejemplo = "Hola Hola"
cantidad_veces = ejemplo.count("Hola")
print("ejemplo.count(a): ",cantidad_veces)

# devuelve el tamaño de una cadena
contar_caracteres = len("ho")
print("Numero de caracteres: ",contar_caracteres)

# verificamos si una cadena empieza con una cadena dada devuelve true, sino false
hola = "Hola Mundo"
empieza_cadena = hola.startswith("o")
print(empieza_cadena)

# verificamos si una cadena termina con una cadena dada devuelve true, sino false
termina_cadena = "Hola Mundo".endswith("o")
print(termina_cadena)

# reemplaza un pedaso de uan cadena dad por otra dada
cadena05 = "Hola Mundo"
cadena_cadena = cadena05.replace("Hola","Que tal?")
print("Nueva cadena: ",cadena_cadena)

# separaar cadenas con las cadenas que le pasemos
tambogrande = "Hola Tambogrande"
cadena_separada = tambogrande.split("....")
print(cadena_separada)