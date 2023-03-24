# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. 
# Каждое число вводится с новой строки.

## a(n) = a(n-1) + d, a(0) = a1, a1 = 1, d = 2, n = 10. a(10) = 1 + 9 * 2 = 19

a = 1
d = 2
n = 10

def a_n(n):
    if n == 1:
        return a
    else:
        return a_n(n - 1) + d 

print(a_n(n))