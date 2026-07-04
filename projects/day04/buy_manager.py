menu_text='''
1. Добавить товар
2. Удалить товар
3. Показать список
4. Выйти
'''
user_answer=int(input(f'{menu_text}'))
shopping_list=list()
while user_answer!=4:
    if user_answer==1:
        shopping_list.append(str(input('Введите название товара для добавления: ')).lower())
        user_answer=int(input(f'{menu_text}'))
    if user_answer==3:
        print(shopping_list)
        user_answer=int(input(f'{menu_text}'))
    if user_answer==2:
        shopping_list.remove(str(input('Введите название товара для удаления: ')).lower())
        user_answer=int(input(f'{menu_text}'))
print('До свидания, приходите еще')