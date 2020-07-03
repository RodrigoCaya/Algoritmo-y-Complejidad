# Pregunta 1
pregunta1 : Pregunta_1/input.txt
	python3 Pregunta_1/pregunta_1.py < Pregunta_1/input.txt > Pregunta_1/pregunta1.txt

# Pregunta 2
pregunta2 : Pregunta_2/input.txt
	python3 Pregunta_2/pregunta_2.py < Pregunta_2/input.txt > Pregunta_2/pregunta2.txt

# Pregunta 3.1
pregunta3.1 : Pregunta_3/3.1/input1.txt
	python3 Pregunta_3/3.1/pregunta_3.1.py < Pregunta_3/3.1/input1.txt > Pregunta_3/3.1/pregunta3.1.txt

# Crear Matriz 3.1
matriz3.1 :
	python3 Pregunta_3/3.1/generarMatriz.py > Pregunta_3/3.1/input1.txt

# Pregunta 3.2
pregunta3.2 : Pregunta_3/3.2/input2.txt
	python3 Pregunta_3/3.2/pregunta_3.2.py < Pregunta_3/3.2/input2.txt > Pregunta_3/3.2/pregunta3.2.txt

# Crear Matriz 3.2
matriz3.2 :
	python3 Pregunta_3/3.2/generarMatriz.py > Pregunta_3/3.2/input2.txt