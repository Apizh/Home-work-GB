import random

# Константа для достижения просветления
NIRVANA_KARMA = 500


# Определение пользовательских исключений
class CustomError(Exception):
    pass


class KillError(CustomError):
    def __str__(self):
        return "Убийство. Вы и убили-с!"


class DrunkError(CustomError):
    def __str__(self):
        return "Пьянство. Пьянству бой!"


class CarCrashError(CustomError):
    def __str__(self):
        return "Вы попали в аварию. Стоит следить за дорогой."


class GluttonyError(CustomError):
    def __str__(self):
        return "Вы обожрались. Следует сократить порции."


class DepressionError(CustomError):
    def __str__(self):
        return "На вас напала хандра. Уныние - грех."


# Список возможных исключений
ERRORS = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]


# Функция, моделирующая один день жизни
def one_day():
    day_karma = random.randint(1, 7)  # Случайное количество кармы от 1 до 7
    if random.randint(1, 10) == 5:  # Случайная вероятность выброса исключения
        raise random.choice(ERRORS)()
    return day_karma


# Основная функция симулятора
def main():
    karma = 0
    with open('karma.log', 'w', encoding='utf-8') as fl_logger:
        while karma < NIRVANA_KARMA:
            try:
                karma += one_day()  # Прибавляем карму за один день
            except CustomError as ex:
                fl_logger.write(f'{ex}\n')  # Записываем информацию об исключении в файл


if __name__ == "__main__":
    main()
    print('Вы достигли Нирваны! ')
    print('Омм')
