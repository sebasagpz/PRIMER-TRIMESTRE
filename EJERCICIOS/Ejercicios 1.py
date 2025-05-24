'''print("--------------------------------------------------")
base = 2
base1 = 3
ex1 = 3
ex2 = 4

op1 = base ** ex1      
op2 = base1 ** ex2     
result = op1 * op2   
print("El resultado de 2^3 x 3^4 es", result)

print("--------------------------------------------------")

base2 = 5
ex3 = 3
ex4 = 2

op3 = ex3 + ex4
result2 = base2 ** op3
print("El resultado de 5^5 * 5^4 es", result2)

print("--------------------------------------------------")

base4 = 10
ex5 = 1
ex6 = 3


op4 = ex5 + ex6
result3 = base4 ** op4
print("El resultado de la operacion 10^1 * 10^ 3 fue", result3)

print("--------------------------------------------------")
base5 = 8
ex7 = 5
ex8 = 2
op5 = ex7 - ex8
result4 = base5 ** op5
print("El resultado de la operación de 8^5/8^2 fue", result4)

print("--------------------------------------------------")

a = "hola que tal"
print(a)

# ESTO ES LLAMADO 'STRING', Cadenas de Texto
nombre = "Hola "
saludo = "Como estás" 
concatenacion = nombre + saludo
print(concatenacion)  

# El print sirve para imprimir algo en la pantalla

# '\n' Sirve para poner una parte del texto arriba e abajo.
print("Hola\nQue tal")

# Print para muchas cosas, se usa 3 comillas dobles
print("""una cadena
otra
otra mas
y muchisimo mas
""")

# Resolver x + 3 = 5
x = 5 - 3
op8= x + 3
print(op8)

# Variables en programación 
# ASIGNACIÓN
# CONCATENACION
# BUSQUEDA
# EXTRACCIÓN
# COMPARACIÓN


HoLa = "hola"
print(HoLa)

mama = "hola"
MAMA = " como estas"

print(mama + MAMA)

variable1 = 1
variable2 = 3
print(variable1 + variable2)

men1 = "Hola"
men2 = "Chola variables 1"

hola3= "Pepito Conejo"

nombre1 = input("Cual es tu nombre? ")
apellido = input("Cual es tu apellido? ")
edad = input("Cuantos años tienes ")
hincha = input("De que equipo eres ")
print("Responde esto porfavor", nombre1)

print("potenciación")
base1=int(input("ingrese base 1"))
exponente1=int(input("ingrese exponente1"))
base2=int(input("ingrese base 2"))
exponente2=int(input("ingrese exponente2"))
op1=base1**exponente1
op2=base2**exponente2 
result=op1*op2
print(f"el resultado de la potenciación fué:",result)
print("-------------------------------------------------------------------------------------")
print("división de potencias")
n1=int(input("ingrese n1"))
exp1=int(input("ingrese exp1"))
n2=int(input("ingrese n2"))
operación1=n1**exp1
operación2=n2**exp1
resultado=operación1/operación2
print(f"el resultado de la operación es:", resultado)
print("--------------------------------------------------------------------------------------")
print("potencia de un producto")
num1=int(input("ingresar num1"))
num2=int(input("ingresar num2"))
exponente=int(input("ingrsar exponente"))
ope1=num1**exponente
ope2=num2**exponente
resultado=ope1*ope2
print(f"el resultado es:", resultado)
print("---------------------------------------------------------------------------------------")


# STRINGS
# INDEXACION EN LAS CADENAS DE TEXTO}

# Asignación (=)

mensaje32= "hola soy mar"
mensaje32 += " salazar"

print(mensaje32)

x, y, z = 34, 2, 3
print(x, y, z)

x, y, z = 34, 2, 3
print(x)
print(y)
print(z)


xd = y = z = 0

x = 10
x = x + 5

print(xd, y, z)
print(x)

# ASIGNACION CON OPERACIONES
n = 10
n += 510
n /= 2
print(n)

# +

# ASIGNACION CON TEXTO
op = "hola "
op+= "que "
op+= "tal"
print(op)

# CONCATENACIÓN
texto1 = "Hola"
texto2 = "Mundo"
resultado = texto1 + " " + texto2
print(resultado)

# BUSQUEDA
texto45 = "El atardecer pintaba el cielo de tonos naranjas y violetas mientras el mar reflejaba cada destello como un espejo en calma. Los pájaros regresaban a sus nidos y el viento suave traía consigo el olor salado del océano, envolviendo el momento en una quietud casi sagrada."

buscar = texto45.find("atardecer")
buscar1 = texto45.find("océano")
print(buscar)
print(buscar1)

# EXTRACCIÓN
extraer = texto45[3:216]
print(extraer)

# COMPARACIÓN
cadena1 = "hola"
cadena2 = "hola"
cadena3 = "Mundo"
print(cadena1 == cadena2)
print(cadena2 == cadena3)

print("-------------------------------------")
# TAREAS

# 1. BÚSQUEDA
palabra= "El conocimiento es poder"
print(palabra.find("conocimiento"))
print(palabra.find("poder"))

# o puede usarse como
# buscar1 = palabra.find("conocimiento")
# print(buscar1)

print("-------------------------------------")
# 2. FIND
palabra2= "La práctica hace al maestro."
print(palabra2.find("práctica"))
print(palabra2.find("maestro."))

print("-------------------------------------")

# TAREA 3
print("-------------------------------------")
frase1 = input("Hola Usuario: Coloca una frase ")
palabra4 = input("Que palabra quieres buscar en la frase: ")
print("La palabra que buscabas esta en la posicion:", frase1.find(palabra4))

# TRAER TEXTO DE INTERNET
google= "Doña Uzeada de Ribera Maldonado de Bracamonte y Anaya era baja, rechoncha, abigotada. Ya no existia razon para llamar talle al suyo. Sus colores vivos, sanos, podian mas que el albayalde y el soliman del afeite, con que se blanqueaba por simular melancolias. Gastaba dos parches oscuros, adheridos a las sienes y que fingian medicamentos. Tenia los ojitos ratoniles, maliciosos. Sabia dilatarlos duramente o desmayarlos con recato o levantarlos con disimulo. Caminaba contoneando las imposibles caderas y era dificil, al verla, no asociar su estampa achaparrada con la de ciertos palmipedos domesticos. Sortijas celestes y azules le ahorcaban las falanges"
print("La palabra Sabia esta en la posicion", google.find(" Sabia"))
print("Desde Caminaba hasta falanges la posicion son:", google.find("Caminaba"), google.find("falanges"))
print(google[459:655])

google2= "La sociedad francesa estaba dividida en estamentos dependiendo de sus clases sociales, el poder mas alto lo tenía el rey, detrás estaban la nobleza y el clero y el nivel mas bajo de poder lo tenia el tercer estado que estaba constituido por la burguesía, los artesanos y los campesinos."
print("La palabra rey esta en la posicion", google2.find("rey"))
print("Desde Caminaba hasta falanges la posicion son:", google2.find("rey"), google2.find("constituido"))
print(google2[117:236])'''

# ACTIVIDAD EXTRA N.1 
print("------------------------------------------------------------")
print("ACTIVIDAD EXTRA N.1")
nombre = input("Bienvenido Usuario, digita tu nombre: ")
nota_1 = float(input("Digita la nota 1: "))
nota_2 = float(input("Digita la nota 2: "))
nota_3= float(input("Digita la nota 3: "))

nota_final = (nota_1 * 0.2) + (nota_2 * 0.3) + (nota_3 * 0.5)
print("Hola", nombre, ", tu nota final es", {nota_final})