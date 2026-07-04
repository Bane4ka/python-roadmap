import random
Balance=100000
while input('Хотите сыграть? (да/нет): ').lower()=='да':
    Bet=int(input(f'''
    Добро пожаловать в казино!
    Ваш баланс:{Balance}
    Выбрать ставку: '''))
    if Bet>Balance:
        print(f'''
        Недостаточно средст на балансе
        Ваш баланс:{Balance}''')
    if Bet<=0:
        print(f'''
        Ставка не может быть меньше или равна нулю'
        Ваш баланс:{Balance}''')
    if Bet>0 and Bet<=Balance:
        rand=random.randint(1, 10)
        if rand==7:
            Balance=Balance+Bet*3
            print(f'''
            Выпало число - {rand}
            Поздравляем вы выиграли (x3)!
            Ваш выигрыш {Bet*3}
            Ваш баланс:{Balance}''')
        elif rand==3:
            Balance=Balance+Bet*2
            print(f'''
            Выпало число - {rand}
            Поздравляем вы выиграли (x2)!
            Ваш выигрыш {Bet*2}
            Ваш баланс:{Balance}''')
        else:
            Balance=Balance-Bet
            print(f'''
            Выпало число - {rand}
            К сожалению вы проиграли, повезет в следующий раз
            Ваш баланс:{Balance}''')
print('До встречи, приходите еще!')



    

    



