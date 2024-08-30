import os
import random

MAGIC_NUMBER = 777


class MagicFileProcessor:
    def __init__(self, filename):
        """Инициализация с именем файла и определение пути к файлу."""
        self.filename = filename
        self.file_path = self.get_file_path()
        self.magic_sum = 0

    def get_file_path(self):
        """Возвращает полный путь к файлу."""
        return os.path.join(os.path.abspath('.'), self.filename)

    def is_exception_raise(self):
        """Возвращает True с вероятностью 1 из 13, чтобы имитировать ошибку."""
        return random.randint(1, 13) == 7

    def pre_init(self):
        """Удаляет файл, если он существует."""
        try:
            os.remove(self.file_path)
        except OSError as ex:
            print(f'{ex}\nДанный файл не может быть удален')

    def process_input(self):
        """Обрабатывает ввод пользователя и записывает его в файл."""
        try:
            input_number = int(input('Введите число: \n'))
            self.magic_sum += input_number
            if self.is_exception_raise():
                raise Exception('Вас постигла неудача!')
            with open(self.file_path, 'a') as out_fd:
                out_fd.write(f"{input_number}\n")
        except (ValueError, KeyboardInterrupt) as ex:
            print(f'{ex}\nВозникли проблемы при вводе.')
            print('Попробуйте еще раз')

    def run(self):
        """Основной метод для запуска процесса обработки ввода."""
        self.pre_init()  # Удаляет старый файл, если он существует
        while self.magic_sum < MAGIC_NUMBER:
            self.process_input()
        print('Вы успешно выполнили условие для выхода из порочного цикла!')


# Запуск программы
if __name__ == "__main__":
    processor = MagicFileProcessor('out_file.txt')
    processor.run()
