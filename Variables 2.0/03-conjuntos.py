print("CONJUNTOS EN PYTHON")

# Creacion de conjuntos => Usando llaves {} directamente
mi_conjunto = {1,2,3,4,5,6}
print(f"Mi conjunto: {mi_conjunto}")

# usando la funcion set()
otro_conjunto = set(["Mango","Limon","Papaya","Pera"])
print(f"Mi otro conjunto: {otro_conjunto}")
 
#Conjunto dentro de otro conjunto
conjunto = set(["Dato 1",])

#Metiendo un conjunto dentro de otra conjunto
mi_conjunto_01 = frozenset(["Dato 01","Dato 02"])
mi_conjunto_02 = {mi_conjunto_01,"Dato 03"}
print(f"Mi conjunto => {mi_conjunto_02}")

# Teoria de conjuntos 
conjunto_01 = {1,3,5,7}
conjunto_02 = {1,3,7}

print(f"Conjunto 01 => {conjunto_01}")
print(f"Conjunto 02 => {conjunto_02}")

# Verificando si conjunto_02 es un subconjunto de conjunto_01
resultado = conjunto_02.issubset(conjunto_01)
resultado_otro = conjunto_02 <= conjunto_01
print(f"conjunto_02.issubset(conjunto_01) => {resultado}")
print(f"conjunto_02 <= conjunto_01 => {resultado_otro}")

# Verificando si conjunto_01 es un superconjunto de conjunto_02
resultado = conjunto_01.issuperset(conjunto_02)
resultado_otro = conjunto_01 >= conjunto_02
print(f"conjunto_01.issuperset(conjunto_02) => {resultado}")
print(f"conjunto_01 >= conjunto_02 => {resultado_otro}")

#verificar si hay algun digito en comun 
hay_digito_comun = conjunto_02.isdisjoint(conjunto_01)
print(f"Digito en comun => {hay_digito_comun}")
