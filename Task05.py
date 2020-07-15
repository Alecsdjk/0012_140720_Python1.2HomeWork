my_list = [7, 5, 3, 3, 2]
us_num = int(input('Enter some integer: '))
for i in my_list:
    if us_num >= i:
        my_list.insert(my_list.index(i),us_num)
        my_list[my_list.index(i) + 1] = my_list[my_list.index(i)]
        break

print(my_list)
