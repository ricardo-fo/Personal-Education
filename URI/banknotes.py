# https://www.urionlinejudge.com.br/judge/en/problems/view/1018
value = int(input())
print(value)
a = value // 100
value %= 100
print("%i nota(s) de R$ 100,00" %a)
b = value // 50
value %= 50
print("%i nota(s) de R$ 50,00" %b)
c = value // 20
value %= 20
print("%i nota(s) de R$ 20,00" %c)
d = value // 10
value %= 10
print("%i nota(s) de R$ 10,00" %d)
e = value // 5
value %= 5
print("%i nota(s) de R$ 5,00" %e)
f = value // 2
value %= 2
print("%i nota(s) de R$ 2,00" %f)
g = value // 1
value %= 1 
print("%i nota(s) de R$ 1,00" %g)