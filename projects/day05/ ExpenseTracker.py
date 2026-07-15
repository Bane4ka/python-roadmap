expenses = {}

def show_menu():
    print('''1. Добавить расход
2. Показать сумму по категориям
3. Показать все расходы
4. Выйти''')

def add_expense(expenses, category, amount):
    if category in expenses:
        expenses[category].append(amount)
    else:
        expenses[category] = [amount]

def show_all(expenses):
    for key, value in expenses.items():
        print(key, value)

def show_totals(expenses):
    for key, value in expenses.items():
        print(key, sum(value))

show_menu()
user_choise = int(input())

while user_choise != 4:

    if user_choise == 1:
        category = input('Введите название категории расходов: ')
        amount = int(input('Введите сумму расхода: '))
        add_expense(expenses, category, amount)

    elif user_choise == 2:
        show_totals(expenses)

    elif user_choise == 3:
        show_all(expenses)

    show_menu()
    user_choise = int(input())

print('Программа завершена')