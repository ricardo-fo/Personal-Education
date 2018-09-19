x = int(input("Informe quantos números você deseja soma: "))
i = 1
soma = 0
while (i <= x):
	a = float(input("0{}- ".format(i)))
	soma += a
	i += 1
print("A soma é {}.".format(soma))