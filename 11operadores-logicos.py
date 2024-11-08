print("OPERADORES LOGICOS")
# AND
resultado01 = True & True       # => TRUE
resultado02 = False & True      # => FALSE
resultado03 = True & False      # => FALSE
resultado04 = False & False     # => FALSE

# OR
resultado05 = True | True       # => TRUE
resultado06 = False | True      # => TRUE
resultado07 = True | False      # => TRUE
resultado08 = False | False     # => FALSE

# NOT
resultado09 = not True          # => FALSE
resultado10 = not False         # => TRUE

print("resultado01 = True & True: ",resultado01)
print("resultado02 = False & True: ",resultado02)
print("resultado03 = True & False: ",resultado03)
print("resultado04 = False & False: ",resultado04)

print("resultado05 = True | True: ",resultado05)
print("resultado06 = False | True: ",resultado06)
print("resultado07 = True | False: ",resultado07)
print("resultado08 = False | False: ",resultado08)

print("resultado09 = not True: ",resultado09)
print("resultado09 = not False: ",resultado10)

# ejemplo 
mayor =  not 5 < 10
print(mayor)