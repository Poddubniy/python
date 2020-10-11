"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for num, el in enumerate(source_list) if source_list[num - 1] < source_list[num]]

print(f'Новый список {new_list[1:]}')


# new_list = []
# num = 0
# for el in my_list:
#     if my_list[num - 1] < my_list[num]:
#         new_list.append(el)
#     num += 1

# for el, new_list in enumerate(my_list):
#     if my_list[el - 1] < my_list[el]:
#         print(new_list)
