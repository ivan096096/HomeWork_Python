# 1.3  Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле в одной строке одно число.

# # Заполняем список
n = int(input('Введите число = '))
my_list = []
for i in range(-n, n + 1):
  my_list.append(i)
print(my_list)

# # Создаём фал
with open("Fail.txt", "w") as fileAdd:
  print(*my_list, file=fileAdd)

# Чтение с файла
Path = 'Fail.txt'
lst = []
with open(Path, 'r') as my_arr:
  data = my_arr.read()
  lst.append(data.split())
  print(lst)
  for i in lst:
    mult = lst[i] + lst[i+1]       #Не мгу понять что не так.перепробывал много
    print(f'Произведение =  {mult}')

