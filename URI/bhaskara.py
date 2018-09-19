# https://www.urionlinejudge.com.br/judge/en/problems/view/1036
import math
a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
delta = b**2 - 4 * a * c
if (a == 0) or (delta < 0):
	print("Impossivel calcular")
else: 
	r1 = (-1 * b + math.sqrt(delta)) / (2 * a)
	r2 = (-1 * b - math.sqrt(delta)) / (2 * a)
	print("R1 = {:.5f}\nR2 = {:.5f}".format(r1,r2))