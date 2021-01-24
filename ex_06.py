# def int_func(word):
#     k = str(word).title()
#     return k
#
#
# l = input('Введите слово: ')
# print(int_func(l))
# print(int_func('camel'))

"""

       Верхняя функция для преобразования одного слова, а нижняя для предложения.

       Но предложение из одного слова никто не отменял, поэтому нижняя функция делает
       то же самое, что и верхняя.

"""

def int_func(word):
    k = str(word).split()
    k_title = []
    for elem in k:
        elem = str(elem).title()
        k_title.append(elem)
    k_title_str = ' '.join(k_title)
    return k_title_str


l = input('Введите предложение:  ')
print(int_func(l))

