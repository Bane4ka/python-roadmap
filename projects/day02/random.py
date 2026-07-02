const=57
user_number=int(input('Введите число: '))
while user_number!=const:
    if user_number>const:
        print('Меньше')
    elif user_number<const:
        print('Больше')
    user_number=int(input('Введите число: '))
print('Примите мои поздравления, вы разгадали число компьютера!')