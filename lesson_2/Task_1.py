# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
#          - 6782 -> 23
#          - 0,56 -> 11
import math
    # Это решение нашёл и инете
n = int(input("Введите число = "))
my_lst = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
print(my_lst)
print(sum(my_lst))
#         не могу разобратся как сложить дробные числа
n = int(input("Введите число  = "))
str1 = str(n)
A = 1
result = []
for i in range(0, len(str1), A):
  result.append(int(str1[i : i + A]))
print(sum(result))




