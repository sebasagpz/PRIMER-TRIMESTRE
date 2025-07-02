# #   EJERCICIO WHILE 
# print(f"Ejercicio 1")
# print("SUMA HASTA CERO")
# total = 0
# n1 = int(input("ingrese un numero (si ingresa 0 el programa se termina): "))
# while n1 != 0:
#     total += n1
#     n1 = int(input("ingrese un numero (si ingresa 0 el programa se termina): "))
#     print(f"la suma total es: {total}")


# print(f"Ejercicio 2")
# print("CONTRASEÑA SECRETA")
# clave = 123
# contraseña = int(input("ingrese el numero de 4 digitos para permitirle el acceso: "))
# while contraseña != clave :
#     print("contraseña incorrecta")
#     contraseña = int(input("ingrese el numero de 4 digitos para permitirle el acceso: "))
# print("ACCESO OTORGADO")



# print(f"Ejercicio 3")
# print("LISTA DE COMPRAS")
# lista = []
# producto = input("ingrese un producto: ".upper())
# while producto != "fin": 
#     lista.append(producto)
#     producto = input("ingrese un producto: ".upper())
# print(f"su listas de producto es la siguiente: {lista}")



# print("Ejercicio 4")
# print("CONTADOR DE PARES O IMPARES")
# num = int(input("Ingrese un numero para saber si es par o impar: "))

# print("Ejercicio 5")
# print(f"PROMEDIO DE CALIFICACIONES")

# notas=[]
# entrada = input(f"Ingrese su nota (0-5)\nescribe SALIR para finalizar el programa: ")
# while entrada.lower() != "salir":
#     nota = float(entrada)
#     if 0<=  nota <=5:
#         notas.append(nota)
#     else:
#         print("Nota invalida")
#     entrada = input(f"Ingrese su nota (0-5)\nescribe SALIR para finalizar el programa: ")

# if notas:
#     promedio=sum(notas)/len(notas)
#     print(f"El promedio: {promedio:.2f}")
# else:
#     print("La nota es invalida")
    
# print("Ejercicio 6")
# num = int(input(f"Ingresa el numero para imprimir su tabla de multiplicación (HASTA LA TABLA DEL 10): "))
# contador = 1
# while contador <=10:
#     resultado = num * contador
#     print(f"{num}  * {contador} = {resultado}")
#     contador +=1
    
# print("Ejercicio 7")
# secret = 17
# gs = int(input("Adivina el número! Ingresa un número: "))

# while gs != secret:
#     if gs < secret:
#         print(f"El número es mayor a {gs}")
#     else:
#         print(f"El número es menor a {gs}")
#     gs = int(input("Intenta de nuevo: "))

# print("¡Felicidades! Adivinaste el número.")

# print("Ejercicio 8")
# tupla1 = ("FRESAS", "MANDARINA", "MANZANA", "PERA", "UVA")
# gs2 = input("Adivina la fruta! Ingresa una fruta: ").upper()

# while gs2 != tupla1:
#     if gs2 not in tupla1:
#         print(f"Buen intento! {gs2} no está en las frutas")
#         gs2 = input("Intenta de nuevo: ").upper()
#     elif gs2 in tupla1:
#         print(f"Adivinaste! {gs2}, si está en la tupla")
#         break
# print(tupla1)

# print("Ejercicio 9")

# diccionario = {
#     "VACA": "COW",
#     "COMIDA" : "FOOD",
#     "HOLA": "HELLO",
#     "JUGO": "JUICE",
#     "ADIOS": "BYE"
# }

# es = input("TRADUCTOR\n ESPAÑOL ----> ENGLISH\n Ingresa una palabra en español para traducirla: ").upper()

# while True:
#     if es == "SALIR":
#         print("Gracias por usar el traductor.")
#         break
#     elif es in diccionario:
#         print(f"La traducción de {es} es: {diccionario[es]}")
#         break
#     else:
#         print(f"La palabra {es} no está en nuestra base de datos :(")
#         es = input("Ingresa otra palabra: ").upper()
        
# print("Ejercicio 10")
# print("CALCULADORA")

# opcion = ""

# while opcion != "5":
#     print("\nMENÚ DE OPCIONES")
#     print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividr\n5. Salir")

#     opcion = input("Elige una opción (1-5): ")

#     if opcion == "1":
#         print("SUMA")
#         num1 = float(input("Primer número: "))
#         num2 = float(input("Segundo número: "))
#         print("Resultado:", num1 + num2)
#     elif opcion == "2":
#         print("RESTA")
#         num1 = float(input("Primer número: "))
#         num2 = float(input("Segundo número: "))
#         print("Resultado:", num1 - num2)
#     elif opcion == "3":
#         print("MULTIPLICACION")
#         num1 = float(input("Primer número: "))
#         num2 = float(input("Segundo número: "))
#         print("Resultado:", num1 * num2)
#     elif opcion == "4":
#         print("DIVISIÓN")
#         num1 = float(input("Primer número: "))
#         num2 = float(input("Segundo número: "))
#         print("Resultado:", num1 / num2)
#     elif opcion == "5":
#         print("Saliendo de calculadora...")
#     else:
#         print("Opción inválida. Intenta de nuevo.")
        
# print("Ejercicio 11")
# print("REGISTRO DE EDADES")

# diccionario1 = {}

# while True:
#     name = input("Ingresa un nombre\nO Escribe SALIR para terminar: ")
#     if name.lower() == "salir":
#         break
#     edad = input("Ingresa la edad de esa persona: ")
#     diccionario1[name] = edad

# print("DICCIONARIO:")
# print(diccionario1)

# print("Ejercicio 12")
# colors = ["NARANJA", "ROJO", "VIOLETA", "DORADO", "AMARILLO"]
# gs3 = input("Ingresa un color: ").upper()

# while gs3 != colors:
#     if gs3 not in colors:
#         print(f"{gs3} no está en la lista")
#         gs3 = input("Intenta de nuevo: ").upper()
#     elif gs3 in colors:
#         print(f"{gs3} sí esta en la lista")
#         break
    
# print("Ejercicio 13")
# num2 = int(input(f"Ingresa el numero para imprimir la potenciación (hasta el 5): "))
# con = 1
# while con <=5:
#     result = num2 ** con
#     print(f"{num2}^{con} = {result}")
#     con +=1
    
print("Ejercicio 14")
print("LISTA DE CUADRADOS")

n = []
contar = 0

while contar < 5:
    num = int(input("Ingresa un número: "))
    cuadrado = num ** 2
    n.append(cuadrado)
    print(f"El cuadrado de {num} es {cuadrado}")
    contar += 1  

print("\nLista de cuadrados ingresados:", n)
print("Finaliza el programa")


print("Ejercicio 15")
print("DICCIONARIO DE ESTUDIANTES")

estu = {}

while True:
    nombre = input("Ingresa el nombre del estudiante (o escribe 'fin' para terminar): ").upper()

    if nombre == "FIN":
        break

    nota = float(input("Ingresa su nota final: "))
    estu[nombre] = nota

print("\nLista completa de estudiantes y notas:")
print(estu)
print("Finaliza el programa")

print("EJERCICIOS WHILE")