# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
 my_list = 'spring ' * 3 + 'summer ' * 3 + 'automn ' * 3 + 'winter ' * 3
 my_list = my_list.split()
 print(my_list[int(input('Enter month as integer: ')) - 1])

my_dict = {3 : 'spring',6 : 'summer', 9 : 'automn', 12 : 'winter'}
m_i = int(input('Enter month as integer: '))
for i in my_dict:
    if  m_i <= i:
        print(my_dict[i])
        break