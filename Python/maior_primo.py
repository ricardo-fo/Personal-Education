def maior_primo(num):
	if num < 0 or num == 0 or num == 1:
		return 1
	else:
		if num % 2 == 0:
			num = num - 1
		z = int(num**(1/2))
		p = False
		for num in range(num, 3, -2):
			for i in range(3, num, 2):
				#print("i = {}, num = {} e p = {}\n".format(i, num, p))
				#print("num / i == {}\n".format(num/i))
				if (num % i) == 0:
					p = False
					break
				else:
					p = True
			if p:
				return num
primo = int(input())
print(maior_primo(primo))