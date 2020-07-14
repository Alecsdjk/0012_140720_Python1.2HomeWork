# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = [9, 6.9, True, 'six', None, complex(6, 9), [6, 9], (6, 9), {6, 9}, {'a': 11}]
print(my_list)

for i in my_list:
    if type(i) is int:
        print(f'{my_list.index(i) + 1}-st element has {type(i)}')
    elif type(i) is float:
        print(f'{my_list.index(i) + 1}-st element has {type(i)}')
    elif type(i) is str:
        print(f'{my_list.index(i) + 1}-st element has {type(i)}')
    elif type(i) is None:
        print(f'{my_list.index(i) + 1}-st element has {type(i)}')
    elif type(i) is complex:
        print(f'{my_list.index(i) + 1}-st element has {type(i)}')
    elif type(i) is list:
        print(f'{my_list.index(i) + 1}-st element has {type(i)}')
    elif type(i) is tuple:
        print(f'{my_list.index(i) + 1}-st element has {type(i)}')
    elif type(i) is set:
        print(f'{my_list.index(i) + 1}-st element has {type(i)}')
    elif type(i) is dict:
        print(f'{my_list.index(i) + 1}-st element has {type(i)}')
    else:
        print(f'{my_list.index(i) + 1}-st element has {type(i)}')


