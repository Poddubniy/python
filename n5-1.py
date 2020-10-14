"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

f_1 = open('n5-1.txt', 'w', encoding='Utf-8')

while True:
    u_text = input('Для выхода нажмите "q" или введите текст: \n')
    f_1.writelines(u_text)
    f_1.write('\n')
    if u_text == 'q' or 'й':
        break
f_1.close()

f_1 = open('n5-1.txt')
block = f_1.readlines()
print(block)
f_1.close()
