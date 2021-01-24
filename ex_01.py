def devision(x, y):
    if y == 0:
        return 'На ноль делить нельзя!'
    else:
        z = x / y
        return z


dividend = float(input('Введите делимое: '))
divisor = float(input('Введите делитель: '))
num = devision(dividend, divisor)
print(num)

