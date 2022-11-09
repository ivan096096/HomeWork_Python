# Вычислить число c заданной точностью d
#
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


def leibnic(n):
    result = 0.0
    list1 = []
    for i in range(1, n, 2):
        result = abs(4.0 / i - result)
        list1.append(result)
    print(list1)


leibnic(int(input('Введите число - ')))
