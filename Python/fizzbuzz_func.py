def fizzbuzz(n):
	if n % 3 == 0:
		if n % 5 != 0:
			return 'Fizz'
		else:
			return 'FizzBuzz'
	elif n % 5 == 0 and n % 3 != 0:
		return 'Buzz'
	else:
		return n

num = int(input())
#print(fizzbuzz(num))