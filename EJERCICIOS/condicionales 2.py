# # EJERCICIO CREDITO BANCARIO

# print("SOLICITUD DE CRÉDITO")

# na = input("Bienvenido Usuario, digite su nombre: ")
# ed = (int(input("Digite su edad: ")))

# if ed < 18:
#     print("No puedes continuar con la solicitud")
# else:
#     ca = (int(input("Digita la cantidad a solicitar: ")))
#     print("Hola", na, "Tu crédito de", ca, "fue aprobado")
    
# # # EJERCICIO SALA DE JUEGOS
# edad2 = (int(input("Bienvenido Usuario, digita tu edad: ")))

# if edad2 < 4:
#     print("----FACTURA SALA DE JUEGOS----\nEdad: ", edad2, "Precio: GRATIS")
# elif edad2 >= 4 and edad2 <= 18:
#     print("----FACTURA SALA DE JUEGOS----\nEdad: ", edad2, "Precio: 5€")
# elif edad2 > 18:
#     print("----FACTURA SALA DE JUEGOS----\nEdad: ", edad2, "Precio: 18€")
# else:
#     print("Edad no valida")
    
# EJERCICIO CALCULADORA

print("CALCULADORA")
print("SUMA = S\nRESTA = R\nMULTIPLICACION = M\nDIVISION = D")

op = (input("Ingresa el operador: ")).upper()
num1 = (float(input("Ingresa el primer numero: ")))
num2 = (float(input("Ingresa el segundo numero: ")))


if op == "S":
    ops = num1 + num2
    print("La suma fue de: ", ops)
elif op == "R":
    opr = num1 - num2
    print("La resta fue de", opr)
elif op == "M":
    opm = num1 * num2
    print("La multiplicacion fue de", opm)
elif op == "D":
    opd = num1 // num2
    opround = round(opd, 2)
    print("La division fue de", opround)