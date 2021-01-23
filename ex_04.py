# def my_func(x, y):
#     if (x == 0 and y < 0):
#         return 'На ноль делить нельзя'
#     else:
#         num = x ** y
#         return num
#
#
# x = float(input('Введите положительное число: '))
# y = int(input('Введите отрицательное целое число: '))
# print(my_func(x, y))

def my_func_2(x, y):
    i = -1
    while i > y:
        b = x
        x *= b
        print(x)
        i -= 1
    return 1 / x


x = float(input('Введите положительное число: '))
y = int(input('Введите отрицательное целое число: '))
print(float(my_func_2(x, y)))

