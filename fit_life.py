# я прочитал что можно использовать try/except, не знал как оно работает, у ИИ
# узнал информацию, какое то время сам посидел поломал голову как оно работает
# и потом узнал что можно делать бесконечные запросы try/except через
# # while True. С while True мне тоже подсказала ИИ.
TEXT_FOR_WEIGHT = 'Введите ваш вес, используя знак "."для указания десятых '
TEXT_FOR_HEIGHT = ('Введите ваш рост в метрах, '
                   'используя знак "." для указания десятых ')
DAYLY_WATER_ML = 30
ML_TO_LITER = 1000  # Количество миллилитров в литрах


def ask_user_weight():
    """Спрашивает вес, если появляется ошибка - уточняет что может быть не так
    и снова спрашивает
    """
    while True:
        try:
            return float(input(TEXT_FOR_WEIGHT))
        except ValueError:
            print('Введите число цифрами, без запятых, используйте точку')


def ask_user_age():
    """Спрашивает возраст, если появляется ошибка - уточняет что может
    быть не так и снова спрашивает
    """
    while True:
        try:
            return int(input('Введите ваш полный возраст цифрами '))
        except ValueError:
            print('Введите число цифрами, без запятых')


def ask_user_height():
    """Спрашивает рост, если появляется ошибка - уточняет что может
    быть не так и снова спрашивает
    """
    while True:
        try:
            return float(input(TEXT_FOR_HEIGHT))
        except ValueError:
            print('Введите число цифрами, без запятых, используйте точку')


user_name = input('Добро пожаловать! Пожалуйста, напишите ваше имя ').title()
user_age = ask_user_age()
user_weight = ask_user_weight()
user_height = ask_user_height()
bmi = round(user_weight / (user_height ** 2), 1)  # индекс массы тела,
# округлённый до десятых
water_l = user_weight * DAYLY_WATER_ML / ML_TO_LITER
print(f'{user_name} ({user_age} лет)! Вот ваши рекомендации:')
print(f'Дневная норма потребления воды: {water_l} л.')
print(f'Ваш индекс массы тела составляет: {bmi}')
