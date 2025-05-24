estudiante = {
    "nombre": "laura",
    "edad" : 25,
    "carrera" : "Ingenieria"
}

print("Hola", estudiante ["nombre"])

nombre_mas = input("¿Cual es el nombre de tu mascota?: ")
tipo = input("¿Cual es el tipo de tu mascota?: ")
edad = (int(input("Cual es la edad?: ")))
nombre_due = input("¿Cual es tu nombre?: ")
ciudad = input("¿En donde te encuentras: ")

mascota = {
    "nombre" : nombre_mas,
    "tipo" : tipo,
    "edad" : edad,
    "dueño" : nombre_due,
    "ciudad" : ciudad
}

print("El nombre de su mascota es:", nombre_mas, "El tipo de mascota es:", tipo, "Su edad:", edad, "Tu nombre es:", nombre_due, "Vives en:", ciudad)
