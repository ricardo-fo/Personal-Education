# https://www.urionlinejudge.com.br/judge/en/problems/view/1013
a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
x = (a + b + abs(a - b)) / 2
maior = (x + c + abs(x - c)) / 2
print("{} eh o maior".format(int(maior)))