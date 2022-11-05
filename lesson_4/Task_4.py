# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from sympy import symbols
from random import randint
from math import prod


def koeficient(k):
  with open('FILE_KOEFF1.txt','w') as file1:
   max_value = 100
   koff =[randint(- max_value,max_value) for i in range(k)]+[randint(1,max_value)]
   x = symbols('x')
   res = (sum(map(prod,zip(koff,[x**i for i in range(k+1)]))),'= 0')
   print(res)
   print(*koff,file =file1)

koeficient(int(input('Введите степень k = ')))

