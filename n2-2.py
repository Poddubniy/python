#2. Для списка реализовать обмен значений соседних элементов, т.е.
#Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
#При нечетном количестве элементов последний сохранить на своем месте.
#Для заполнения списка элементов необходимо использовать функцию input().

list_data = []
x = 0
index = 0

q = int(input('Сколько будет чисел в списке? '))

while x < q:
    list_data.append(int(input('Введите число: ')))
    x += 1

for n in range(int(len(list_data)/2)):
    list_data[index], list_data[index + 1] = list_data[index + 1], list_data[index]
    index += 2

print(list_data)