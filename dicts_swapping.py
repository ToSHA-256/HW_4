import time
from datetime import datetime


# Task 1
def dict_swap(dict_arg):
    var_dict = {}
    for key, value in dict_arg.items():
        var_dict[value] = key
    return var_dict


print(f'\n#1. Замена ключей на значения и наоборот:')
dict1 = {'a': '2', 'c': 5}
print(dict1)
dict2 = dict_swap(dict1)
print(dict2)


# Task 2
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


var = ''
while not var.isdigit():
    print(f'\n#2. Вычисление факториала. Введите число:')
    var = input()
var = int(var)
print(var)
res = factorial(var)
print(f'{var}! = {res}')


# Task 3*
def symbols_stat(in_list):
    var_dict = {}
    for i in in_list:
        if i in var_dict.keys():
            var_dict[i] += 1
        else:
            var_dict[i] = 1
    return var_dict


input_list = [1, 2, 4, 5, 32, 4, 3, 2, 1, 1, 5, 5]
print(f'\n#3. Подсчёт статистики символов в:')
print(input_list)
stat = symbols_stat(input_list)
for key, value in stat.items():
    print(f'Число {key} встречается {value} раз')


# Task 4*
def generate_list(num):
    var_list = []
    while num > 0:
        time.sleep(1)
        var_list.append(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        yield var_list[-1]
        num -= 1

print(f'\n#4. Генератор времменных меток: ')
print('Введите количество: ')

numbers = int(input())
gen_list = generate_list(numbers)
for i in range(0, numbers):
    print(next(gen_list))
