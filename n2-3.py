#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

month_list = ['зима', 'весна', 'лето', 'осень']
month_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}

month_number = abs(int(input('Введите любую цифру от 1 до 12: ')))

if month_number <= 12:
    if month_number == 12 or month_number == 1 or month_number == 2:
        print(month_list[0])
        print(month_dict[1])
    elif month_number == 3 or month_number == 4 or month_number == 5:
        print(month_list[1])
        print(month_dict[2])
    elif month_number == 6 or month_number == 7 or month_number == 8:
        print(month_list[2])
        print(month_dict[3])
    elif month_number == 9 or month_number == 10 or month_number == 11:
        print(month_list[3])
        print(month_dict[4])
else:
    print('На земле нет такого месяца')
