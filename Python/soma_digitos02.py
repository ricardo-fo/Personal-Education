n = input("Digite um número inteiro: ")
tam = len(n)
i = soma = 0
while i < tam:
	soma = soma + int(n[i])
	i += 1
print(soma)