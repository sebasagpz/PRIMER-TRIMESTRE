print ("Sistema de Calificaciones")
print(f"Es un sistema en Python que calcula el promedio de tres notas por materia y muestra el resultado al usuario.")
print("---------------------------------------------------- \n")
nombre = input("Bienvenido Usuario, ingresa tu nombre: ")

# MATERIA 1
mate1 = input("Ingresa nombre de la primera materia: ")
nota1 = float(input("¿Cual es tu primera nota?: "))
nota2 = float(input("¿Cual es tu segunda nota?: "))
nota3 = float(input("¿Cual es tu tercera nota?: "))

opa = nota1 + nota2 + nota3
op1 = opa // 3
print("Hola", nombre, ", tu nota de", mate1, "fué ", op1)

# MATERIA 2
print("---------------------------------------------------- \n")
mate2 = input("Ingresa nombre de la segunda materia: ")
nota4 = float(input("¿Cual es tu primera nota?: "))
nota5 = float(input("¿Cual es tu segunda nota?: "))
nota6 = float(input("¿Cual es tu tercera nota?: "))

opb = nota1 + nota2 + nota3
op2 = opb // 3
print("Hola", nombre, ", tu nota de", mate2, "fué ", op2)

# MATERIA 3
print("---------------------------------------------------- \n")
mate3 = input("Ingresa nombre de la segunda materia: ")
nota7 = float(input("¿Cuál es tu primera nota?: "))
nota8 = float(input("¿Cuál es tu segunda nota?: "))
nota9 = float(input("¿Cuál es tu tercera nota?: "))

opc = nota7 + nota8 + nota9
op3 = opc // 3  
print(f"Hola {nombre}, tu nota de {mate3} fue {op3}")

# MATERIA 4
print("---------------------------------------------------- \n")
mate4 = input("Ingresa nombre de la tercera materia: ")
nota10 = float(input("¿Cuál es tu primera nota?: "))
nota11 = float(input("¿Cuál es tu segunda nota?: "))
nota12 = float(input("¿Cuál es tu tercera nota?: "))

opd = nota10 + nota11 + nota12
op4 = opd // 3
print(f"Hola {nombre}, tu nota de {mate4} fue {op4}")

# MATERIA 5
print("---------------------------------------------------- \n")
mate5 = input("Ingresa nombre de la cuarta materia: ")
nota13 = float(input("¿Cuál es tu primera nota?: "))
nota14 = float(input("¿Cuál es tu segunda nota?: "))
nota15 = float(input("¿Cuál es tu tercera nota?: "))

ope = nota13 + nota14 + nota15
op5 = ope // 3
print(f"Hola {nombre}, tu nota de {mate5} fue {op5}")
