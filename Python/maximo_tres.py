def maximo(n1, n2, n3):
	if n1 > n2:
		if n1 > n3:
			return n1
		else:
			return n3
	else:
		if n2 > n3:
			return n2
		else: 
			return n3
		if n1 == n2:
			return n1
		elif n1 == n3:
			return n3
		elif n2 == n3:
			return n3

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(maximo(num1, num2, num3))