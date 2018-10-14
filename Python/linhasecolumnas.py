row = int(input("digite a largura: "))
column = int(input("digite a altura: "))
a = True
for z in range(0, column, 1):
	if(a):
		print('#' * row)
		a = False
		continue
	if(z == column - 1):
		print('#' * row)
		break
	if(row > 3):
		print('#', ' ' * (row - 4), '#')
	elif(row == 3):
		print("# #")
	elif(row == 2):
		print("##")
	else:
		print('#')