# https://www.urionlinejudge.com.br/judge/en/problems/view/1021
# This answer help me to solve the problem with the floating points in these values
# https://pt.stackoverflow.com/questions/44715/como-arredondar-um-float-em-python
value = float(input())

# NOTES :
print("NOTAS:")

hundred = value // 100
print("%i nota(s) de R$ 100.00" %hundred)
value = value - hundred * 100
#print("100 - value = {}\n".format(value))

fifty = value // 50
print("%i nota(s) de R$ 50.00" %fifty)
value = value - fifty * 50
#print("50 - value = {}\n".format(value))

twenty = value // 20
print("%i nota(s) de R$ 20.00" %twenty)
value = value - twenty * 20
#print("20 - value = {}\n".format(value))

ten = value // 10
print("%i nota(s) de R$ 10.00" %ten)
value = value - ten * 10
#print("10 - value = {}\n".format(value))

five = value // 5
print("%i nota(s) de R$ 5.00" %five)
value = value - five * 5
#print("05 - value = {}\n".format(value))

two = value // 2
print("%i nota(s) de R$ 2.00" %two)
value = value - two * 2
#print("02 - value = {}\n".format(value))

# COINS:
print("MOEDAS:")

one = value // 1
print("%i moeda(s) de R$ 1.00" %one)
value = value - one
value = round(value,2)
#print("01 - value = {}\n".format(value))

fifty_cents = value // 0.5
print("%i moeda(s) de R$ 0.50" %fifty_cents)
value = value - fifty_cents * 0.5
value = round(value,2)
#print("0.5 - value = {}\n".format(value))

twenty_five_cents = value // 0.25
print("%i moeda(s) de R$ 0.25" %twenty_five_cents)
value = value - twenty_five_cents * 0.25
value = round(value,2)
#print("0.25 - value = {}\n".format(value))

ten_cents = value // 0.1
print("%i moeda(s) de R$ 0.10" %ten_cents)
value = value - ten_cents * 0.1
value = round(value,2)
#print("0.1 - value = {}\n".format(value))

five_cents = value // 0.05
print("%i moeda(s) de R$ 0.05" %five_cents)
value = value - five_cents * 0.05
value = round(value,2)
#print("0.05 - value = {}\n".format(value))

one_cent = value / 0.01
print("%i moeda(s) de R$ 0.01" %one_cent)
value = value - one_cent * 0.01
value = round(value,2)
#print("0.01 - value = {}\n".format(value))