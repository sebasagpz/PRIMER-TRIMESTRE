# EJERCICIO 1

producto = input("Ingresa el nombre del producto: ")
precio = (float(input("Ingresa el precio: ")))
cantidad = (int(input("¿Cuantas unidades compraste?: ")))

tupla1 = (producto, precio)
lista1 = (tupla1, cantidad)

diccionario = {
    "producto" : lista1
}

op = precio * cantidad
print(f"El costo total de", producto, "fué", op)

# EJERCICIO 2

n1 = input("Ingresa el primer producto: ")
p1 = (int(input("Ingresa el precio del primer producto: ")))
c1 = (int(input("¿Cuantas cantidades compraste?: ")))

n2 = input("Ingresa el segundo producto: ")
p2 = (int(input("Ingresa el precio del segundo producto: ")))
c2 = (int(input("¿Cuantas cantidades compraste?: ")))

n3 = input("Ingresa el tercer producto: ")
p3 = (int(input("Ingresa el precio del tercer producto: ")))
c3 = (int(input("¿Cuantas cantidades compraste?: ")))

tn1 = (n1, p1)
tn2 = (n2, p2)
tn3 = (n3, p3)

li1 = [tn1, c1]
li2 = [tn2, c2]
li3 = [tn3, c3]

dic = {
    "producto1" : li1,
    "producto2" : li2,
    "producto3" : li3
}

o1 = p1 * c1
o2 = p2 * c2
o3 = p3 * c3

print("El costo total de", n1, "es de", o1)
print("El costo total de", n2, "es de", o2)
print("El costo total de", n3, "es de", o3)


# EJERCICIO 3
name = input("Bienvenido usuario, ingresa tu nombre: ")
m1 = input("Ingresa la asignatura 1: ")
n1m1 = float(input("Ingresa la nota 1: "))
n2m1 = float(input("Ingresa la nota 2: "))

m2 = input("Ingresa la asignatura 2: ")
n1m2 = float(input("Ingresa la nota 1: "))
n2m2 = float(input("Ingresa la nota 2: "))

m3 = input("Ingresa la asignatura 3: ")
n1m3 = float(input("Ingresa la nota 1: "))
n2m3 = float(input("Ingresa la nota 2: "))

tup1 = (n1m1 + n2m1 / 2)
tup2 = (n1m2 + n2m2 / 2)
tup3 = (n1m3 + n2m3 / 2)

lis1 = [tup1, n1m1, n2m1]
lis2 = [tup2, n1m2, n2m2]
lis3 = [tup1, n1m3, n1m3]

listo = [lis1, lis2, lis3]

dic3 = {
    "nombre" : name,
    "materias" : listo,
}

promfinal = tup1 + tup2 + tup3
mate = promfinal // 3
print("BOLETIN DE CALIFICACIONES")
print("------------------------------------------------------")
print("Hola", name, "Este es tu boletin de calificaciones:")
print("Materia", m1, "Promedio: ", tup1)
print("Materia", m2, "Promedio: ", tup2)
print("Materia", m3, "Promedio: ", tup3)
print("Promedio Final: ", mate)