def vogal(character):
	vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
	if character in vowels:
		return True
	else:
		return False

string = input()
vogal(string)