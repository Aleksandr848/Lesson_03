def my_func(a, b, c):
    min_num = min(a, b, c)
    sum_number = a + b + c - min_num
    return sum_number


nums = input('Введите три числа через пробел: ').split()
print(my_func(int(nums[0]), int(nums[1]), int(nums[2])))

