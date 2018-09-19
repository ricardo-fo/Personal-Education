a = int(input("Informe um número: "))
controle = True
while controle and a != 0:
	anterior = (a // 10) % 10
	print(anterior)
	print("a % 10", a % 10)
	if(a % 10 == anterior):
		controle = False
		break
	a = a // 10
	print('a =',a)
if controle:
	print("não")
else:
	print("sim")