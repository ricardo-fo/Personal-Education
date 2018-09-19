def fatorial(n):
	while True:
		fat = 1
		try:
			if n > 0:
				while(n > 1):
					fat = fat * n
					n = n - 1
				return fat
			elif n == 0:
				return 1
			elif n == 1:
				return 1
		except (n < 0):
			print("Enter a value greater 0.")

def binomial(n, k):
	return (fatorial(n)) / (fatorial(k) * fatorial(n - k))