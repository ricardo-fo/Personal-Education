n = int(input("Digite um número inteiro: "))
if(n % 2 == 0):
	print("não primo")
else:
	raiz = int(n**(1/2))
	controle = True
	i = 3
	while(i <= raiz):
		if(n % i == 0):
			break
		i += 2
	if(i > raiz):
		print("é primo")
	else:
		print("não primo")
