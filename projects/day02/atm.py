Balance=int(input('Введите баланс: '))
Znach=int(input('1. Проверить баланс'
' 2. Пополнить'
' 3. Снять деньги'
' 4. Выйти'))
if Znach==1:
    print(f'Ваш баланс:{Balance}')
    Znach=int(input('1. Проверить баланс'
' 2. Пополнить'
' 3. Снять деньги'
' 4. Выйти'))
if Znach==2:
    Add=int(input('Введите сумму пополнения: '))
    Balance=Balance+Add
    Znach=int(input('1. Проверить баланс'
' 2. Пополнить'
' 3. Снять деньги'
' 4. Выйти'))
if Znach==3:
    Take=int(input('Сколько снять?'))
    if Balance>=Take: 
        Balance=Balance-Take
    else: print('Недостаточно средств(ты бомж)')
    Znach=int(input('1. Проверить баланс'
' 2. Пополнить'
' 3. Снять деньги'
' 4. Выйти'))
if Znach==4:print('Пока пока')