num = int(input("Informe um número inteiro: "))
i = 1
soma = 0
copia = num
tam = len(str(num))

while (i <= tam):
	dig = int(num % 10)
	soma += dig
	num = (num - dig) / 10
	i += 1
print("A soma dos dígitos de {} é {}.".format(copia,soma))