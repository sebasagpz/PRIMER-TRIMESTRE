num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
num4 = int(input("Ingrese el cuarto número: "))
num5 = int(input("Ingrese el quinto número: "))
num6 = int(input("Ingrese el sexto número: "))
num7 = int(input("Ingrese el séptimo número: "))
num8 = int(input("Ingrese el octavo número: "))
num9 = int(input("Ingrese el noveno número: "))
num10 = int(input("Ingrese el décimo número: "))

lista1 = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]

tupla1 = tuple(lista1)

tupla2 = (num1, num1 ** 2)
tupla3 = (num2, num2 ** 2)
tupla4 = (num3, num3 ** 2)
tupla5 = (num4, num4 ** 2)
tupla6 = (num5, num5 ** 2)
tupla7 = (num6, num6 ** 2)
tupla8 = (num7, num7 ** 2)
tupla9 = (num8, num8 ** 2)
tupla10 = (num9, num9 ** 2)
tupla11 = (num10, num10 ** 2)

lista2 = [tupla2, tupla3, tupla4, tupla5, tupla6, tupla7, tupla8, tupla9, tupla10, tupla11]

smt = sum(lista1)
prom = smt // len(lista1)
doblesm = smt * 2
mitadpr = prom // 2


print("La suma total de los numeros ingresados es:", smt)
print("El promedio de sus numeros es: ", prom)
print("El doble de la suma de sus datos es: ", doblesm)
print("La mitad del promedio de los numeros es", mitadpr)

lista3 = [num2 * num5,
          num7 * num8,
          num3 // num4,
          num1 - num9,
          num6 + num10]

