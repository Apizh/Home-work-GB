class Book:
    _id_counter = 1

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls._id_counter
        cls._id_counter += 1
        return instance

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book(ID={self.id}, title={self.title}, author={self.author})"


# Пример использования
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
print(book1)
print(book2)
