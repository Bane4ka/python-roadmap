from math import *
dollar_price = 77.0
rubles_count=float(input('Введите количество рублей: '))
dollars_count=round(rubles_count/dollar_price, 2)
print(f'В {rubles_count} рублях {dollars_count} долларов')