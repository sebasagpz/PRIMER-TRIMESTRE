# EJERCICIOS DE TUPLA
print("EJERCICIOS DE TUPLAS")
print("-----------------------------------------------")

# Ejercicio 1: Crea una tupla con los numeros del 1 al 5
tupla_1 = (1, 2, 3, 4, 5)

# Ejercicio 2: Muestra el segundo valor de la tupla creada anteriormente
print(tupla_1[1])

# Ejercicio 3: Imprime cuantos elementos tiene una tupla
print("La tupla_1 tiene", len(tupla_1), "elementos")

# Ejercicio 4: Encuentra la posición del numero 4 en la tupla
print("La posición del numero 4 es", tupla_1.index(4))

# Ejercicio 5: Cuantas veces aparece el numero 2 en la tupla
print("El numero 2, aparece", tupla_1.count(2), "vez")

# Ejercicio 6: Crea una tupla que contenga una cadena de texto, un numero entero y un numero decimal
tupla_2 = ("Hola", 2, 3.5)

# Ejercicio 7: Crea una que contenga otra tupla en su interior. Luego accede al primer valor de la tupla interna

tupla_3 = (tupla_2)
print(tupla_3[0]) 
