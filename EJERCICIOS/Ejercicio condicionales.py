señor = int(input("Bienvenido señor, digite su año de nacimiento: "))


if señor <= 1920:
    print("Generación no registrada")
elif señor <= 1946:
    print("Usted es generación Silenciosa")
elif señor <= 1964:
    print("Usted es Baby Boomer")
elif señor <= 1979:
    print("Usted es Generación X")
elif señor <= 2000:
    print("Usted es Generación Y")
elif señor <= 2010:
    print("Usted es Generación Z")
else:
    print("Edad de nacimiento no valida")