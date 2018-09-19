# https://www.urionlinejudge.com.br/judge/en/problems/view/1017
hours = int(input())
speed = int(input())
liter = (speed / 12) * hours
print("{:.3f}".format(liter))