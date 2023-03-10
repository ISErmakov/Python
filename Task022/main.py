# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
import random

n = int(input("Enter n: "))
list_n = [random.randrange(1, 100) for _ in range(n)]

m = int(input("Enter m: "))
list_m = [random.randrange(1,100) for _ in range(m)]

print(list_n)
print(list_m)


set_nm = set(list_m)
set_nm = set_nm.union(list_n)
list_nm = list(set_nm)
list.sort(list_nm)

print(list_nm)