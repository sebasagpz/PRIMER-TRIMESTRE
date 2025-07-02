Algoritmo EDADs
	Escribir "¿Cuál es tu edad?"
	Leer edad
	
	Si edad <= 11 Entonces
		Escribir "Es un niñ@"
	SiNo
		Si edad > 11 Y edad <= 17 Entonces
			Escribir "Es un adolescente"
		SiNo
			Si edad >= 18 Y edad <= 25 Entonces
				Escribir "Es un adulto"
			SiNo
				Escribir "Es un adulto mayor"
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
