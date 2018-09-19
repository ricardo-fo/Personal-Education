num = int(input("Digite o valor de n: "))
if(num == 0):
	controle = False
else:
	controle = True

num_copia = fatorial = num
while controle:
	num_copia = num_copia - 1
	if(num_copia == 0):
		controle = False
		break
	fatorial = fatorial * num_copia
if(num != 0):
	print(fatorial)
else:
	print(1)