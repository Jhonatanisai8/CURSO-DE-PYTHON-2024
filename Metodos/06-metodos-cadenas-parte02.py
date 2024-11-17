"¡Hola programadores! Hoy les traigo un top de métodos útiles para trabajar con cadenas en Python. ¡Vamos a darle caña al código! 💻🔥"
# Métodos de manipulación básica
# Convierte todos los caracteres de la cadena a mayúsculas.
"hola".upper()  # "HOLA"
# Convierte todos los caracteres a minúsculas
"HoLA".lower()  # "hola"
# Convierte la primera letra en mayúscula y el resto en minúsculas.
"python es genial".capitalize()  # "Python es genial"
# Convierte la primera letra de cada palabra en mayúscula.
"python es genial".title()  # "Python Es Genial"
# Elimina espacios (u otros caracteres especificados) al inicio y al final de la cadena.
"  hola  ".strip()  # "hola"
# Elimina espacios al inicio de la cadena.
"  hola".lstrip()  # "hola"
# Elimina espacios al final de la cadena.
"hola  ".rstrip()  # "hola"

# Métodos de búsqueda y reemplazo
# Devuelve el índice de la primera aparición de sub. Si no se encuentra, devuelve -1.
"hola mundo".find("mundo")  # 5
# Similar a find(), pero lanza una excepción si no encuentra sub.
"hola mundo".index("mundo")  # 5
# Reemplaza todas las ocurrencias de old por new.
"hola mundo".replace("mundo", "Python")  # "hola Python"
# Cuenta cuántas veces aparece sub en la cadena.
"hola hola".count("hola")  # 2
# Métodos para dividir y unir
# Divide la cadena en una lista usando delim como separador (por defecto, espacios).
"uno,dos,tres".split(",")  # ['uno', 'dos', 'tres']
# Igual que split() pero comienza desde el final de la cadena.
"uno,dos,tres".rsplit(",", 1)  # ['uno,dos', 'tres']

# Métodos de validación
# Devuelve True si todos los caracteres son letras.
"hola".isalpha()  # True
# Devuelve True si todos los caracteres son números.
"123".isdigit()  # True
# Devuelve True si todos los caracteres son letras o números.
"hola123".isalnum()  # True
# Devuelve True si la cadena contiene solo espacios en blanco.
"   ".isspace()  # True


