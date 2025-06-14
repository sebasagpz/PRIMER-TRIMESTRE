#  Ejercicios con Condicionales y Operaciones Matemáticas
# 1. Verifica si un numero es positivo, negativo o cero


print(f"-----------TALLER CONDICIONALES-----------")

print(f"EJERCICIO 1")
n1 = (float(input("Ingresa un numero a verificar: ")))

if n1 > 0:
    print("El numero es positivo")
elif n1 < 0:
    print("El numero es negativo")
elif n1 == 0:
    print("El numero es 0")
else:
    print("Hubo un error")

print(f"EJERCICIO 2")

n2 = (float(input("Ingresa un primer numero a verificar: ")))
n3 = (float(input("Ingresa un segundo numero a verificar: ")))

if n2 > n3:
    print("El numero", n2, "es mayor a", n3)
elif n3 > n2:
    print("El numero", n3, "es mayor a", n2)
elif n2 < n3:
    print("El numero", n2, "es menor a", n3)
elif n3 < n2:
    print("El numero", n3, "es menor a", n2)
else:
    print("Este no es un numero válido")

print(f"EJERCICIO 3")

n4 = (float(input("Ingresa un numero a verificar: ")))


print(f"EJERCICIO 4")

n5 = (float(input("Ingresa el numero a verificar: ")))

if n5 >= 10 and n5 <= 20:
    print("Está entre 10 y 20")
else:
    print("No está entre 10 y 20")

print(f"EJERCICIO 5")

n6 = float(input("Ingresa el primer numero: "))
n7 = float(input("Ingresa el segundo numero: "))
n8 = float(input("Ingresa el tercer numero: "))

if n6 > n7 and n6 >= n8:
    print("El numero", n6, "es mayor")
elif n7 > n6 and n7 >= n8:
    print("El numero", n7, "es mayor")
else:
    print("El numero", n8, "es mayor")

print(f"EJERCICIO 6")

pfin = (float(input("Ingresa el precio final del producto: ")))

if pfin > 100:
    por = pfin * 0.10
    des = pfin - por
    print("El total fue de", des)
else:
    print("No es mayor a 100$")
    
print(f"EJERCICIO 7")

ed1 = int(input("Bienvenido, para votar debes ingresar tu edad: "))

if ed1 >= 18:
    print("Puedes votar")
else:
    print("Eres menor de edad, no puedes votar")
    
print(f"EJERCICIO 8")

vn = (input("Bienvenido Usuario, ¿Eres VIP o NORMAL?: ")).upper()
n9 = (float(input("Ingresa el precio del producto: ")))

if vn == "VIP":
    por1 = n9 * 0.20
    des2 = n9 - por1
    print("Bienvenido cliente VIP, su precio es de", des2)
else:
    print("Bienvenido cliente NORMAL, su precio es de", n9)

#  Ejercicios con Condicionales y Operaciones Matemáticas
# 2. Ejercicios con Listas (con condicionales)

print (f"EJERCICIO 9")
print("Determinar si el  numero es multiplo de 3 y 5")

nu99=int(input("Ingrese un numero:"))
if nu99%3==0 and nu99%5==0:
    print("El numero es multiplo de 3 y 5 al  mismo tiempo")
elif nu99%3==0:
    print("El numero solo es multiplo de 3")
elif nu99%5==0:
    print("El numero solo es multiplo de 5")
else:
    print("El numero no es multiplo ni de 3 ni de 5")

#------------------------------------------------------------------------------------

print(f"EJERCICIO 10")
print("Determinar si el numero es divisible entre otros")

n101= int(input("Ingrese el numero para verificar  si es divisible:"))
n102= int(input("Ingrese el primer numero  para verificar si es divisor:"))
n103= int(input("Ingrese el segundo numero para verificar si es divisor:"))
if n101%n102==0 and n101//n103==0:
    print("El numero es divisible por los dos numeros")
elif n101%n102==0:
    print ("El  numero solo es divisible por:",n2)
elif n101%n103==0:
    print("El numero solo es divisible por:",n3)
else:
    print("El numero no es divisible por ninguno de los dos numeros")

print(f"EJERCICIO 11")
pre111 = (int(input(f"Ingrese un primer numero: ")))
pre112 = (int(input(f"Ingrese un segundo numero: ")))
pre113 = (int(input(f"Ingrese un tercer numero: ")))
pre114 = (int(input(f"Ingrese un cuarto numero: ")))
pre115 = (int(input(f"Ingrese un quinto numero: ")))
lista1 = [pre111, pre112, pre113, pre114, pre115]

print(lista1)
if lista1[2] > 10:
    print("es Mayor a 10")
elif lista1[2] <= 10:
    print("es menor o igual a 10")
    

# print(f"EJERCICIO 12")
pre121 = (int(input(f"Ingrese un primer numero: ")))
pre122 = (int(input(f"Ingrese un segundo numero: ")))
pre123 = (int(input(f"Ingrese un tercer numero: ")))
pre124 = (int(input(f"Ingrese un cuarto numero: ")))
pre125 = (int(input(f"Ingrese un quinto numero: ")))
lista2 = [pre121, pre122, pre123, pre124, pre125]
if 7 in lista2:
    print("El numero 7 SI está en la lista")
else:
    print("El numero 7 NO está en la lista")

print("EJERCICIO 13")
list00=[4, 6, 2, 8]
sume = list00[0] + list00[1]
if sume > 10:
    print("Suma alta")
else:
    print("Suma baja")

print(f"EJERCICIO 14")
print("Nombre correcto")
name= ["Ana", "Luis", "Pedro", "Marta"]
ulti_name= name[-1]  
if ulti_name == "Marta":
    print("Nombre correcto")
else:
    print("Nombre diferente")

print(f"EJERCICIO 15")
print("Lista de colores")
colors= ["magenta", "azul", "dorado"]
print(colors)
if colors[1] == "azul":
    colors[1] = "amarillo" 
    print(f"Se ha actualizado la lista {colors}")
else:
    print("La lista no se ha actualizado")



print(f"EJERCICIO 16")
print("Orden ascendente o descendente")
tupla00= (5, 8, 12, 20)
print(tupla00)
if tupla00[0] < tupla00[-1]:
    print("Orden ascendente")
else:
    print("Orden descendente")
    
print(f"EJERCICIO 17")
tupla5 = (25, 32, 28)
if tupla5[1] > 30:
    print("Edad mayor a 30")
else:
    print("Edad menor o igual a 30")

print(f"EJERCICIO 18")
tup23=(1,2,3)
listac = list(tup23)
if listac [1] == 2:
    listac[1] == 10
tuplc = tuple[listac]
print(tuplc)



print(f"EJERCICIO 19")
tupla7 = (4, 9)
if tupla7[1] > 5:
    print("Coordenada alta")
else:
    print("Coordenada baja")

print(f"EJERCICIO 20")
tupla8 = (3, 4)
tupla9 = (3, 5)
if tupla8 == tupla9:
    print("Tuplas iguales")
else:
    print("Tuplas diferentes")

print(f"EJERCICIO 21")
dic1 = {"nombre": "Juan", "edad": 17}
if dic1["edad"] >= 18:
    print("Adulto")
else:
    print("Menor de edad")

print(f"EJERCICIO 22")
dic2 = {"nombre": "Lucía", 
        "edad": 20}
if dic2["edad"] > 18:
    dic2["edad"] = 21
print(dic2)

print(f"nEJERCICIO 23")
dic3 = {"nombre": "Carlos"}
if "ciudad" not in dic3:
    dic3["ciudad"] = "Bogotá"
print(dic3)

print(f"EJERCICIO 24")
dic4 = {"producto": "pan", "precio": 1200}
if "precio" in dic4:
    print(dic4["precio"])
else:
    print("No hay precio")

print(f"EJERCICIO 25")
dic5 = {"pan": 1200, 
        "leche": 2000}
if "pan" in dic5:
    print(dic5["pan"])
else:
    print("Producto no disponible")
