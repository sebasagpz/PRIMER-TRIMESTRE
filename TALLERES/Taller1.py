print("TALLLER 1 MAYO 3")
print("--------------------------------------------")

#  Ejercicio 1
print("Ejercicio 1")
num_1 = int(input("Digita numero 1: "))
num_2 = int(input("Digita numero 2: "))
op_1= num_1 + num_2

print("Hola, el resultado de la suma fué", op_1)

# Ejercicio 2
print("--------------------------------------------")
print("Ejercicio 2")
num_3 = int(input("Digita numero 1: "))
num_4 = int(input("Digita numero 2: "))
op_2= num_3 - num_4
print("Hola, el resultado de la resta fué", op_2)

# Ejercicio 3
print("Ejercicio 3")
print("--------------------------------------------")
num_5 = int(input("Digita numero 1: "))
num_6 = int(input("Digita numero 2: "))
op_3= num_5 * num_6
print("Hola, el resultado de la multiplicación fué", op_3)

# Ejercicio 4
print("Ejercicio 4")
print("--------------------------------------------")
num_7 = int(input("Digita numero 1: "))
num_8 = int(input("Digita numero 2: "))
op_4= num_7 / num_8
print("Hola, el resultado de la división fué", op_4)

# Ejercicio 5
print("Ejercicio 5")
print("--------------------------------------------")
nombre = input("Bienvenido Usuario, digita tu nombre: ")
apellido = input("Ahora digita tu apellido: ")
print("Has ingresado correctamente:", nombre, apellido)

# Ejercicio 6
print("Ejercicio 6")
print("--------------------------------------------")

nombre = input("Bienvenido Usuario, digita tu nombre: ")
print("La primera letra de tu nombre es:", nombre[0])

# Ejercicio 7
print("Ejercicio 7")
print("--------------------------------------------")

nombre = input("Bienvenido Usuario, digita tu nombre: ")
print("La primera letra de tu nombre es:", nombre[-1])

# Ejercicio 8
print("Ejercicio 8")
print("--------------------------------------------")
base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))
op_5 = base * altura
print("La area del rectangulo con base", base, "y altura", altura, "es:", op_5)

# Ejercicio 9
print("Ejercicio 9")
print("--------------------------------------------")

nacimiento = int(input("Bienvenido usuario, digita tu año de nacimiento: "))
actual = 2025
op_6 = actual - nacimiento
print("En 2025, tienes", op_6, "años")

# Ejercicio 10
print("Ejercicio 10")
print("--------------------------------------------")
usuario = input("Digita tu Usuario: ")
dominio = input("Digita el Dominio: ")
correo = usuario + "@" + dominio
print("Tu dirección de correo electronico es", correo)

# Ejercicio 11
print("Ejercicio 11")
print("--------------------------------------------")
nombre_2 = input("Digita tu nombre: ")
print(len(nombre_2))

# EJercicio 12
print("Ejercicio 12")
print("--------------------------------------------")
palabra1 = input("Digita la primera palabra: ")
palabra2 = input("Digita la segunda palabra: ")
concatenacion = palabra1 + " " + palabra2
print(concatenacion)

# Ejercicio 13
print("Ejercicio 13")
print("--------------------------------------------")
palabra3 = input("Digita la palabra: ")
print("La segunda letra es", palabra3[1])

# Ejercicio 14
print("Ejercicio 14")
print("--------------------------------------------")
palabra4 = input("Digita la palabra: ")
print("Las tres primeras letras son", palabra4[0] + palabra4[1] + palabra4[2])


# Ejercicio 15
print("Ejercicio 15")
print("--------------------------------------------")
palabra5 = input("Digita la palabra: ")
print("Palabra invertida:", palabra5[::-1])


# Ejercicio 16
print("Ejercicio 16")
print("--------------------------------------------")
num_8 = int(input("Ingresa el primer número: "))
num_9 = int(input("Ingresa el segundo número: "))
print("Suma:", num_8 + num_9)
print("Resta:", num_8 - num_9)
print("Multiplicación:", num_8 * num_9)
print("División:", num_8 / num_9)

# Ejercicio 17
print("Ejercicio 17")
print("--------------------------------------------")
num_10 = int(input("Ingresa un número: "))
print("El doble es:", num_10 * 2)

# Ejercicio 18
print("Ejercicio 18")
print("--------------------------------------------")
num_11 = int(input("Ingresa un número: "))
print("La mitad es:", num_11 // 2)

# Ejercicio 19
print("Ejercicio 19")
print("--------------------------------------------")
frase_1 = input("Ingresa una frase: ")
print("Cantidad de caracteres:", len(frase_1))

# Ejercicio 20
print("Ejercicio 20")
print("--------------------------------------------")
palabra_2 = input("Ingresa una palabra: ")
print("Repetida 3 veces:", palabra_2 + " " + palabra_2 + " " + palabra_2)

# Ejercicio 21
print("Ejercicio 21")
print("--------------------------------------------")
nom_2 = input("Bienvenido usuario, digite su nombre: ")
print("Las segundas primeras letras son", nom_2[0] + nom_2[1])
print("Las segundas ultimas letras son", nom_2[-2] + nom_2[-1])

# Ejercicio 22
print("Ejercicio 22")
print("--------------------------------------------")
frase_2 = input("Bienvenido usuario, coloca una frase (solo impar de letras): ")
medio_22 = len(frase_2)
print("Letra del medio:", frase_2[medio_22 // 2])

# Ejercicio 23
print("Ejercicio 23")
print("--------------------------------------------")
frase_3 = input("Ingresa una frase: ")
print("Primeros 10 caracteres:", frase_3[:10])

# Ejercicio 24
print("Ejercicio 24")
print("--------------------------------------------")
num_17 = int(input("Ingresa un numero: "))
op_5 = num_17 * num_17
print("El numero", num_17, "elevado al cuadrado es: ", op_5)

# Ejercicio 25
print("Ejercicio 25")
print("--------------------------------------------")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese un segundo numero: "))

res= a*(a>=b)+b*(b>a)
print(res)


# Ejercicio 26
print("Ejercicio 26")
print("--------------------------------------------")
edad_20 = int(input("Ingresa tu edad: "))
print("Has vivido aproximadamente", edad_20 * 365, "dias.")

# Ejercicio 27
print("Ejercicio 27")
print("--------------------------------------------")
palabra_27 = input("Bienvenido usuario, ingresa una palabra (cinco letras): ")
print("Letras por separado:")
print(palabra_27[0])
print(palabra_27[1])
print(palabra_27[2])
print(palabra_27[3])
print(palabra_27[4])

# Ejercicio 28
print("Ejercicio 28")
print("--------------------------------------------")
palabra_28 = input("Ingresa una palabra: ")
respuesta_5 = "Tiene más de 5 letras" * (len(palabra_28) > 5)
print(respuesta_5)

# Ejercicio 29
print("Ejercicio 29")
num_23 = int(input("Ingresa un número: "))
print("El numero multiplicado por 10 es", num_23 * 10)

# Ejercicio 30
