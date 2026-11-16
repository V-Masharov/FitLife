# я прочитал что можно использовать try/except, не знал как оно работает, у ИИ
# узнал информацию, какое то время сам посидел поломал голову как оно работает
# и потом узнал что можно делать бесконечные запросы try/except через
# # while True. С while True мне тоже подсказала ИИ.
TEXT_FOR_WEIGHT = 'Введите ваш вес, используя знак "."для указания десятых '
TEXT_FOR_HEIGHT = 'Введите ваш рост в метрах, '
'используя знак "." для указания десятых '


def user_weights():
    """Спрашивает вес, если появляется ошибка - уточняет что может быть не так
    и снова спрашивает
    """
    while True:
        try:
            user_weight_number = float(input(TEXT_FOR_WEIGHT))
            return user_weight_number
        except ValueError:
            print('Введите число цифрами, без запятых, используйте точку')


def user_ages():
    """Спрашивает возраст, если появляется ошибка - уточняет что может
    быть не так и снова спрашивает
    """
    while True:
        try:
            user_age_number = int(input('Введите ваш полный возраст цифрами '))
            return user_age_number
        except ValueError:
            print('Введите число цифрами, без запятых')


def user_heights():
    """Спрашивает рост, если появляется ошибка - уточняет что может
    быть не так и снова спрашивает
    """
    while True:
        try:
            user_heiht_number = float(input(TEXT_FOR_HEIGHT))
            return user_heiht_number
        except ValueError:
            print('Введите число цифрами, без запятых, используйте точку')


user_name = input('Добро пожаловать! Пожалуйста, напишите ваше имя ').title()
user_age = user_ages()
user_weight = user_weights()
user_height = user_heights()
bmi = round(user_weight / (user_height ** 2), 1)  # индекс массы тела,
# округлённый до десятых
water_ml = user_weight * 30  # норма воды в миллилитрах
water_l = water_ml / 1000  # переводим миллилитры в литры
print(f'{user_name} ({user_age} лет)! Вот ваши рекомендации:')
print(f'Дневная норма потребления воды: {water_l} л.')
print(f'Ваш индекс массы тела составляет: {bmi}')
