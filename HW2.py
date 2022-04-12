
# задание 1

name = 55
li = [123, 'Март', 34.5, True, False, name]

for el in li:
    print (f'{el} тип данных: {type(el)}')

# задание 2

li = str (input ('Введите элементы списка:')).split()

for i in range (1, len (li), 2):
    li [i-1], li [i]= li [i], li [i-1]

print (li)



# задание 3

season = { "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11], "Зима": [12, 1, 2]}
mon = int (input('Номер месяца:'))

for el in season:
    if mon in season [el]:
        print (el)
mont = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12]
mont = int (input ('Введите месяц'))
season = ['Зима', 'Весна', 'Лето', 'Осень']
if mont in [1, 2, 12]:
    print (f'{mont}-й месяц относится к {season[0]}')
elif mont in [6, 7, 8]:
    print (f'{mont}-й месяц относится к {season[3]}')
elif mont in [3, 4, 5]:
    print (f'{mont}-й месяц относится к {season[1]}')
elif mont in [9, 10, 11]:
    print (f'{mont}-й месяц относится к {season[2]}')

else:
    print ('Такого месяца не существует')

# задание 4
str = input ('Введите символы, разделяя пробелами:').split()
for i, element in enumerate(str, 1):
    print (f'{i}. {element [:10]}')

# задание 5
number = int(input('Введите число рейтинга:'))
my_list = [7, 5, 3 ,3 ,2]
i=0
for el in my_list:
    if number <= el:
        i+=1
my_list.insert(i,number)
print (my_list)


# задание 6

goods = {'Название':'','Цена':'', 'Количество':'', 'Ед. измерения':''}
res = {'Название':[],'Цена':[], 'Количество':[], 'Ед. измерения':[]}
cort = []
for el in goods:
    m = input (f'Ввведите данные: {el}')
    goods [el]= int (m) if el == 'Цена' or el == 'Количество' else m
cort.append ((i, goods))
print (cort)

for key, value in res.items():
    print (f'{key}:{value}')
