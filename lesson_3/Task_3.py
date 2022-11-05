# 3.Задайте список из вещественных чисел.
# Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# num = math.modf(1.1)
# print(num)

list2 = []
lst = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(lst)):
  result = lst[i] - int(lst[i])
  list2.append(result)
for i in range(len(list2)):
  nums_max = max(list2)
  nums_min = min(list2)
  res = nums_max - nums_min
  print(float(res))

