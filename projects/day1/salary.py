stavka=int(input("Введите ставку: "))
hours=int(input("Введите количество часов: "))
salary=(stavka*hours)*(1-0.13)
nalog=salary*0.13
print(f'Ваша зарплата: {salary} рублей')
print(f'Налог: {nalog} рублей')
