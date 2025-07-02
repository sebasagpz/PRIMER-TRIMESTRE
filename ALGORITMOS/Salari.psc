Algoritmo Salario
	plata <- 1433500
	Escribir "¿Tienes vivienda propia? (si/no)"
	Leer vivienda
	Escribir "¿Cuántos hijos tienes?"
	Leer hijos
	Si vivienda='no' Entonces
		gasto_vivienda <- plata*0.30
	SiNo
		gasto_vivienda <- 0
	FinSi
	gasto_hijos <- hijos*(plata*0.10)
	gasto_servicios <- plata*0.005
	gasto_alimentos <- plata*0.40
	gasto_total <- gasto_vivienda+gasto_hijos+gasto_servicios+gasto_alimentos
	sobrante <- plata-gasto_total
	Escribir 'Gasto en vivienda: $', gasto_vivienda
	Escribir 'Gasto por hijos: $', gasto_hijos
	Escribir 'Gasto en servicios públicos: $', gasto_servicios
	Escribir 'Gasto en alimentos: $', gasto_alimentos
	Escribir 'Total de gastos: $', gasto_total
	Escribir 'Te sobra: $', sobrante
FinAlgoritmo
