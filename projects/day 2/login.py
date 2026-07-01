login='admin'
password='12345'
count_fails=3
while count_fails!=0:
    user_login=str(input('Введите логин: '))
    user_password=str(input('Введите пароль: '))
    if user_login==login and user_password==password:
        print('Добро пожаловать!')
        break
    else:
        count_fails=count_fails-1
        print(f"Неверный логин или пароль. У вас осталось {count_fails} попыток")
if count_fails==0:
    print('Попытки кончились повторите через 20 минут')