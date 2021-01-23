sum_of_numbers = 0
flag = True
while flag:
    numbers = input('Введите числа через пробел.  Для выхода введите "no": ').split()
    for number in numbers:
        if number != 'no':
            number = int(number)
            sum_of_numbers += number
        else:
            flag = False
            break
    print(sum_of_numbers)
