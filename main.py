from pyrogram import Client
from time import sleep

app = Client('my_account')

true_or_false = True

while true_or_false:
    print('1. Ебнуть\n2. Выйти')
    inp = input('> ')
    if inp == '1':
        print('Введите юзернейм пользователя')
        id_ = input('> ')
        try:
            print('ебашим')
            i = 1000
            chat_id = id_
            with app:
                while i > 1:
                    i -= 7
                    text = f'{i+7} - 7 = {i}'
                    app.send_message(chat_id, text)
                    sleep(0.1)
        except Exception:
            print('Пользователь не найден или что то пошло по пизде')
    else:
        true_or_false = False
