from func_soma import soma

x, y = input("INFORME X E Y: ").split(" ")
x = int(x)
y = int(y)
soma = soma(x,y)
print("x + y = {}".format(soma))