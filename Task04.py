# Пользователь вводит строку из нескольких слов,
# разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
my_list = input('Enter some words,separated by spaces: ')

my_list = my_list.split(' ')
cnt = 0
for i in my_list:
    cnt += 1
    print(f'{cnt}. {i}')