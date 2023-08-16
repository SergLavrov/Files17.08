
# 2. Пишем программу с двумя действиями :
# запись в файл, чтение из файла, - и меню. while True ... ,
# затем по пунктам меню - выполнение вышеуказанных операций.

import os
from functions import *

os.system('cls')

sent = input('Input sentence: ')
sentence = sent.split(' ')
# print(sentence)

os.system('pause')
os.system('cls')

while True:

    choice = input_choice()

    if choice == '0':
        break

    elif choice == '1':
        write_to_file(sentence)

    elif choice == '2':
        read_from_file()

    else:
        print('Invalid choice')

    os.system('pause')
    os.system('cls')

print('Goodbye')
