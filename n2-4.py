#4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
#Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

print('list dict tuple false true cowabungaaa')

words = input('Введите несколько слов разделённых пробелами: ')

my_word = []
num = 1
for i in range(words.count(' ') + 1):
    my_word = words.split()
    if len(str(my_word)) <= 10:
        print(f"{num} {my_word[i]}")
        num += 1
    else:
        print(f"{num} {my_word[i] [0:10]}")
        num += 1