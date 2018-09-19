#EXERCÍCIO DO CURSO Introdução à Ciência da Computação com Python Parte 1
#EXERCÍCIO DA SEMANA 3 - Praticar tarefa de programação: Exercícios adicionais (opcionais)
#EXERCÍCIO: 1
import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
dab = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
if (dab >= 10):
	print("longe")
else:
	print("perto")