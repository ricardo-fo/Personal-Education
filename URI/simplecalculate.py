# https://www.urionlinejudge.com.br/judge/en/problems/view/1010
# it help me to find a way to solve this issue: https://pt.stackoverflow.com/questions/230522/entrada-de-n%C3%BAmeros-na-mesma-linha-em-python
# product 1:
a1, b1, c1 = input().split(" ")
code1 = int(a1)
units1 = int(b1)
price1 = float(c1)

# product 2:
a2, b2, c2 = input().split(" ")
code2 = int(a2)
units2 = int(b2)
price2 = float(c2)

# to pay it:
topay = (units1 * price1 + units2 * price2)
print("VALOR A PAGAR: R$ {:.2f}".format(topay))