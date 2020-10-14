"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать
 данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

with open('n5-7.txt', encoding='UTF-8') as file:
    firms = file.read().splitlines()
    dict_firms = {}
    dict_av = {}
    i = 0
    prof_sum = 0
    firm_av = []

    for el in firms:
        firm_doc = el.split()
        profit = int(firm_doc[2]) - int(firm_doc[3])
        dict_firms[firm_doc[0]] = profit
        if profit > 0:
            prof_sum += profit
            i += 1
        else:
            print('Фирма {0} терпит убытки, убытки составили {1}'.format(firm_doc[0], abs(profit)))

    average_profit = round((prof_sum / i), 2)
    dict_av['average_profit'] = average_profit
    firm_av.append(dict_firms)
    firm_av.append(dict_av)
    print(firm_av)

json_firms = json.dumps(firm_av)
print(json_firms)
