import math
xa = int(input('введите первую координату Xa - '))
xb = int(input('введите вторую координату Xb - '))
ya = int(input('введите первую координату Ya - '))
yb = int(input('введите вторую координату Yb - '))

AB = float(math.sqrt(( xb- xa) ** 2)+ ((yb - ya) ** 2))
print(f'Длинна - {AB}')
