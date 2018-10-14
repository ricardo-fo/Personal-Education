"""
Escreva a função n_primos que recebe um número inteiro maior ou igual a 2 
como parâmetro e devolve a quantidade de números primos que existem entre 2 
e n (incluindo 2 e, se for o caso, n).
"""
def is_prime(number):
	fator = 3
	if(number == 2):
		return True
	elif(number <= 1):
		return False
	elif(number % 2 == 0):
		return False
	while(fator <= number / 2):
		if(number % fator == 0):
			return False
		fator = fator + 2
	return True

def n_primos(num):
	z = num
	cont = 0
	while(z >= 2):
		if(is_prime(z)):
			cont = cont + 1
		z = z - 1
	return cont

verify = int(input("Informe um inteiro maior ou igual a 2: "))
print(n_primos(verify))