from pyrogram import Client
from time import sleep
from colorama import init, Fore

init(autoreset=True)

app = Client('my_account')

true_or_false = True

while true_or_false:
    print(Fore.CYAN + '1. Ебнуть\n2. Выйти')
    inp = input('> ')
    if inp == '1':
        print(Fore.CYAN + 'Введите юзернейм пользователя')
        chat_id = input('> ')
        try:
            print(Fore.GREEN + 'ебашим')
            i = 1000
            with app:
                while i > 1:
                    i -= 7
                    text = f'{i+7} - 7 = {i}'
                    app.send_message(chat_id, text)
                    sleep(0.1)
        except Exception:
            print(Fore.RED + 'ERROR\nПользователь не найден или что то пошло по пизде')
    else:
        true_or_false = False
