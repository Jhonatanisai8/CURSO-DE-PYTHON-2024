print("OPERADORES DE COMPARACION")
"""
== es igual que 
!= es distinto que
<  es menor que
<= es menor o igual que
>  es mayor que
>= es mayor o igual que
"""

numero_01 = 5
numero_02 = 6

es_igual_que = (numero_02==numero_01)
es_distinto_que = (numero_01 != numero_02)
es_menor_que = (numero_01 < numero_02)
es_menor_o_igual_que = (numero_01 <= numero_02)
es_mayor_que = (numero_01 > numero_02)
es_mayor_igual_que = (numero_01 >= numero_02)

#calculos combinados
a = 5
b = 10
c = 20

comparacion = a + b < c

#comparacion de usuarios
usuario_tiktok = "jhonatan_isai9"
usuario_tiktok_02 = "daniel_eli_29"

son_iguales = usuario_tiktok == usuario_tiktok_02

#comparar contraseñas
pasword_user_01 = "admin01"
pasword_user_ingresado = "admi01"


print(es_igual_que)
print(es_distinto_que)
print(es_menor_que)
print(es_menor_o_igual_que)
print(es_mayor_que)
print(es_mayor_igual_que)
print("resultado comparativo: ",comparacion)
print("son iguales los usuarios: ",son_iguales)
print("son iguales las contraseñas: ",(pasword_user_01==pasword_user_ingresado))
