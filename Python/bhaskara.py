#EXERCÍCIO DO CURSO Introdução à Ciência da Computação com Python Parte 1
#EXERCÍCIO DA SEMANA 3 - Praticar tarefa de programação: Exercícios adicionais (opcionais)
#EXERCÍCIO: 2
import math

a = float(input())
b = float(input())
c = float(input())
delta = b**2 - 4*a*c
if (delta >= 0):
	#x1 = ((-b + (delta**(1/2)))/2*a)
	x1 = ((-b + (math.sqrt(delta)))/(2*a))
	if (delta != 0):
		#x2 = ((-b - (delta**(1/2)))/2*a)
		x2 = ((-b - (math.sqrt(delta)))/(2*a))
		if (x1 > x2):
			print("as raízes da equação são {} e {}".format(x2,x1))
		else:
			print("as raízes da equação são {} e {}".format(x1,x2))
	else:
		print("a raiz desta equação é {}".format(x1))
else:
	print("esta equação não possui raízes reais")