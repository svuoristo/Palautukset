class Publication:
    def __init__(self, name):
        self.name = name

class Magazine(Publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)

    def print_data(self):
        print(f"{self.name}, päätoimittanut {self.editor}.")

class Book(Publication):
    def __init__(self, name, author, pages):
        self.author = author
        self.pages = pages
        super().__init__(name)

    def print_data(self):
        print(f'{self.name}, kirjoittanut {self.author}, {self.pages} sivua.')

donald_duck = Magazine("Aku Ankka", "Aki Hyyppä")
hytti_no_6 = Book("Hytti n:o 6", "Rosa Liksom", 200)

donald_duck.print_data()
hytti_no_6.print_data()