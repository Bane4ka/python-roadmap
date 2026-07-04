balance = int(input('Введите баланс: '))
def show_menu():
    '''Выводит меню действий для пользователя'''
    print('''1. Проверить баланс
2. Пополнить
3. Снять деньги
4. Выйти''')
def is_valid_amount(balance,amount):
    '''Проверяет, достаточно ли средств на балансе для снятия'''
    if amount<=balance:
        return True
    else: return False

def deposit(balance,amount):
    '''Пополняет баланс на указанную сумму'''
    return balance+amount
def withdraw(balance,amount):
    '''Снимает деньги со счета, если достаточно средств, иначе выводит сообщение о недостатке средств'''
    if is_valid_amount(balance,amount):
        return balance-amount
    else:
        print('Недостаточно средств (ты бомж)')
        return balance
user_answer=0
while user_answer!=4:
    show_menu()
    user_answer=int(input('Выберите действие: '))
    if user_answer==1:
        print(f'Ваш баланс: {balance}')
    if user_answer==2:
        amount=int(input('Введите сумму для пополнения: '))
        balance=deposit(balance,amount)
        print(f'Ваш баланс: {balance}')
    if user_answer==3:
        amount=int(input('Введите сумму для снятия: '))
        balance=withdraw(balance,amount)
        print(f'Ваш баланс: {balance}')
print('До свидания, приходите еще')
