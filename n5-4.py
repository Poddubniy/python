"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []

with open('n5-4.txt', encoding='Utf-8') as numerals:

    for i in numerals:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])

with open('n5-4-1.txt', 'w', encoding='Utf-8') as numerals_write:
    numerals_write.writelines(new_file)

with open('n5-4-1.txt', encoding='Utf-8') as numerals_write:
    n = numerals_write.readlines()
    print(n)
