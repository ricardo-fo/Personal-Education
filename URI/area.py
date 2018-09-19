# https://www.urionlinejudge.com.br/judge/en/problems/view/1012
#it taking the input:
a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
tri_area = ((a * c) / 2)
cir_area = (3.14159 * c ** 2)
tra_area = (((a + b) * c) / 2)
sqr_area = (b ** 2)
rec_area = (a * b)
print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}".format(tri_area,cir_area,tra_area,sqr_area,rec_area))