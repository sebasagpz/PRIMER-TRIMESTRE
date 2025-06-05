# edad = int(input("Cual es tu edad?: "))
# if edad >= 18:
#     print('Es adulto')
# else:
#     print('Es niño')
    
# # PYTHON CONDICIONALES
# # ES IGUAL A: a == b
# # NO ES IGUAL A: a != b
# # MENOS QUE: a < b
# # MENOR O IGUAL QUE: a <= b
# # MAYOR QUE: a > b
# # MAYOR O IGUAL QUE: a >= b

# # ELSE
# ## Es un hermano del 'if' el cual se puede encadenar al final de un bloque del codigo if para comprobar los casos contrarios, es decir los falses

# x = 15
# if x > 10:
#     print("por enccima de diez, ")
#     if x > 20:
#         print("y tambien por encima de 20!")
#     else:
#         print("pero no por encima de 20")
    


# EJERCICIO 1
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))

a = n1 * n2

if a == 4:
    print(a, "es igual a cuatro")
elif a == 5:
    print(a, "es igual a cinco")
elif a == 6:
    print(a, "es igual a seis")
else:
    print("No se cumple la condición")