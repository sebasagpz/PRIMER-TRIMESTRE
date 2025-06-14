# contador = (int(input("Ingresa un  numero: ")))
# while contador > 0:
#     print("Contador:", contador)
#     contador -= 1
    
while True:
    texto = input("Escribe algo (o escribe 'salir para terminar): ").upper()
    if texto == "SALIR":
        break
    print("Escribiste: ", texto)
