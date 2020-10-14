"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

f_2 = open('n5-2.txt', encoding='Utf-8')
content = f_2.read()
print(f'Текст песни: \n{content}\n')
f_2.close()

f_2 = open('n5-2.txt', encoding='Utf-8')
sum_lines = f_2.readlines()
print(f"Кол-во строк: {len(sum_lines)}")
f_2.close()

f_2 = open('n5-2.txt', encoding='Utf-8')
i = 0
while i < len(sum_lines):
    i += 1
    lines_words = f_2.readline()
    print(f"Кол-во слов в {i}-й строке: {len(lines_words.split())}")
f_2.close()

f_2 = open('n5-2.txt', encoding='Utf-8')
content = f_2.read()
print(f"\nОбщее кол-во слов: {len(content.split())}")

f_2.close()
