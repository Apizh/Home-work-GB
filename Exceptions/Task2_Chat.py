class Chat:
    def __init__(self, filename='chat.txt'):
        self.filename = filename

    def display_messages(self):
        """Отображает все сообщения из файла."""
        try:
            with open(self.filename, 'r') as file:
                print(file.read())
        except FileNotFoundError:
            print("Служебное сообщение: пока что ничего нет\n")

    def add_message(self, name, message):
        """Добавляет новое сообщение в файл."""
        with open(self.filename, 'at') as file:
            file.write(f"{name}: {message}\n")

    def run(self):
        """Запускает основной цикл чата."""
        name = input("Как вас зовут? \n")
        while True:
            response = input("Чтобы увидеть текущий текст чата введите 1, чтобы написать сообщение введите 2: ")
            if response == '1':
                self.display_messages()
            elif response == '2':
                self.add_message(name, input("Введите сообщение: "))
            else:
                print("Неизвестная команда\n")


# Запуск программы
if __name__ == "__main__":
    Chat().run()
