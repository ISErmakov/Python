# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
list_n = [random.randrange(1, 100) for _ in range(10)]
print(*list_n)
min_number = int(input("Enter min"))
max_number = int(input("Enter max"))
for i in range(len(list_n)):
    if min_number <= list_n[i] <= max_number:
        print(i)