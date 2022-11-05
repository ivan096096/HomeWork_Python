# 5.Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]



# def fib(n):
#   if n == 1:
#     return 1
#   elif n == 0:
#     return 0
#   else :
#     return  fib(n - 2) + fib(n - 1)

# for i in range(int(input('Введите число - '))):
#   print(fib(i))


# не могу понять что делаю не так?
def fib(n):
 fib1 = fib2 = 1
 print(fib1,fib2,end = ' ')
 for i in range(2,n):
  fib1,fib2 = fib2,fib1 - fib2
  print(fib2,end = ' ')

fib(int(input('введите число фиб - ')))