# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = [23, 34.34, False, "str", [1, 2]]
my_list.append(input('Enter some element in list: '))
my_list.append(input('Enter some another element in list: '))
f_li = None
s_li = None
step = 0
if len(my_list) % 2 != 0:
    last_i = my_list[len(my_list) - 1]
print(my_list)
for i in my_list:
    step += 1
    if i != last_i and step % 2 != 0:
        s_li = my_list[my_list.index(i) + 1]
        my_list[my_list.index(i) + 1] = my_list[my_list.index(i)]
        my_list[my_list.index(i)] = s_li
        print(my_list)
    elif i != last_i and step % 2 == 0:
        continue
    else:
        print(my_list)

