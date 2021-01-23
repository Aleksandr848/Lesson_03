def print_user_data(name, surname, year_of_birth, city, email = 'Нет', phone_num = 'Нет'):
    user_data = f'{name} {surname}, год рождения - {year_of_birth}, родился в городе {city}, эл. почта - {email}, номер телефона - {phone_num}'
    return user_data


user = print_user_data('Александр', 'Максимов', 1978, 'Livani', 'sm-1@inbox.lv')
print(user)

