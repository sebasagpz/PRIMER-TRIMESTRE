mi_tupla = (1,2,3,4)
otra_tupla = ("Hola", "como", "estas", "?")

numeros = (1,2,1,3,1,4,1,5)
numeros.index(5)

numeros.count(1)

# SI SE ENCUENTRA UN VALOR FUERA DE LA TUPLA, AUTOMATICAMENTE GENERA UN ERROR, Porque no está dentro de la tupla
print("Cantidad de numeros 1:", numeros.count(1))

print("Posicion del numero 5:", numeros.index(5))


# EJEMPLO DE LISTA UTILIZANDO 'APPEND' -> que significa agregar algo a la lista (NO SE PUEDE UTILIZAR EN TUPLA)

tareas = ["comer", "leer", "ejercitarse", "estudiar"]
tareas.append("dormir")
print(tareas)

# CONVERTIR TUPLA A LISTA
una_tupla = (1, 2, 3)
una_lista = list(una_tupla)
print(una_lista)

# CONVERTIR LISTA A TUPLA
a_lista = [4, 5, 6]
otra_tupla = tuple(a_lista)
print(otra_tupla)