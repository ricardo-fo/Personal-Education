cont = 0
for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
	if letter in "AEIOU":
		cont += 1
		print(cont, letter, "is a vowel")
	else:
		cont += 1
		print(cont, letter, "is a consonant") 
