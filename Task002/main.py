# 
# Задача 2: Найдите сумму цифр трехзначного числа.
# 
# *Пример:*
# 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

a = int(input('Enter A: '))

print(a // 100 + (a % 100) // 10 + a % 10) 