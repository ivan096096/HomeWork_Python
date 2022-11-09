# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
from operator import add
arr = []
arr2 = []
Path1 = 'FILE_KOEFF1.txt'
with open(Path1, 'r') as File:
    for y in File:
        arr.append(list(map(int,y[:-1].split())))
        print(arr)

Path1 = 'FILE_KOEFF.txt'
with open(Path1, 'r') as read_File:
    for i in read_File:
        arr2.append(list(map(int,i[:-1].split())))
        print(arr2)


def sum_():
 resalt = []
 resalt = [sum(i) for i in zip(arr, arr2 )]  # Что делаю не так перебрал кучу вариантов,везде добавляет второй массив
 print(str(resalt))                             # в конец первого.
sum_()