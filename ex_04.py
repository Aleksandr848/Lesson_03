def my_func(x, y):
    if (x == 0 and y < 0):
        return 'На ноль делить нельзя'
    else:
        num = x ** y
        return num


x = float(input('Введите положительное число: '))
y = int(input('Введите отрицательное целое число: '))
print(my_func(x, y))

def my_func_2(x, y):
    if (x == 0 and y < 0):
        return 'На ноль делить нельзя'
    else:
        i = -1
        b = x
        while i > y:
            x *= b
            i -= 1
    return 1 / x


x = float(input('Введите положительное число: '))
y = int(input('Введите отрицательное целое число: '))
print((my_func_2(x, y)))
