# https://www.urionlinejudge.com.br/judge/en/problems/view/1008
employee = int(input())
hours = int(input())
received = float(input())
salary = hours * received
print("NUMBER = {}\nSALARY = U$ {:.2f}".format(employee,salary))