"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('n5-3.txt', encoding='Utf-8') as staff:
    money = []
    personnel = []
    staff_list = staff.read().split('\n')
    for i in staff_list:
        i = i.split()
        if int(i[1]) < 20000:
           personnel.append(i[0])
        money.append(i[1])

print(f'Оклад меньше 20 тыс.:\n {personnel} \n\nсредний оклад {sum(map(int, money)) / len(money)}')


