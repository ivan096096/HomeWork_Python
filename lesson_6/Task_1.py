# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение
# Формат: Объясняет преподаватель
#
# Задача: предложить улучшения кода для уже решённых задач:
#
# С помощью использования **лямбд, map, zip, list comprehension
# В этом случае можно пропустить совсем тривиальные
# (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.


#   Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def sum_numbers():
 numbers_list = [2, 3, 5, 9, 3]
 sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
 odd_el = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
 print(f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')

sum_numbers()


#     Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
n = input('Введите вещественное число: ')
sum = sum(map(int, n.replace('.', '')))
print (sum)



from functools import reduce

dot_1 = list(map(int, input('Введите две координаты первой точки A, через пробел: ').split()))
dot_2 = list(map(int, input('Введите две координаты второй точки B, через пробел: ').split()))

def dot_range(dot_1, dot_2):
    rng = reduce(lambda x, y: (x + y)**(1/2), (map(lambda dot: (dot[1] - dot[0])**2, zip(dot_1, dot_2))))
    return round(rng, 2)
print(dot_range(dot_1, dot_2))