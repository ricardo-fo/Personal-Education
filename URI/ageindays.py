# https://www.urionlinejudge.com.br/judge/en/problems/view/1020
days = int(input())
years = days // 365
days = days % 365
months = days // 30
days = days % 30
print("{} ano(s)\n{} mes(es)\n{} dia(s)".format(years,months,days))