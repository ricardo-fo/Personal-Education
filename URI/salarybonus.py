# https://www.urionlinejudge.com.br/judge/en/problems/view/1009
name = input()
salary = float(input())
sale = float(input())
salary_final = salary + (sale * 0.15)
print("TOTAL = R$ {:.2f}".format(salary_final))