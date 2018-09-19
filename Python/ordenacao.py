#EXERCÍCIO DO CURSO Introdução à Ciência da Computação com Python Parte 1
#EXERCÍCIO DA SEMANA 3 - Tarefa de programação: Lista de exercícios - 2
#EXERCÍCIO: 5
a = float(input())
b = float(input())
c = float(input())
if ((a < b) and (a < c) and (b < c)):
	print("crescente")
else:
	print("não está em ordem crescente")