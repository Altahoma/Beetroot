class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f'name:{self.name}, country:{self.country}, birthday:{self.birthday}, books:{len(self.books)}'

    def __str__(self):
        return f'{self.name} was born on {self.birthday}, {self.country}. Write {len(self.books)} book(s).'

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)


class Book:
    total = 0

    def __init__(self, name, year, author):
        self.id = Book.total
        self.name = name
        self.year = year
        self.author = author

        Book.total += 1

    def __repr__(self):
        return f'id:{self.id}, name:{self.name}, year:{self.year}, author:{self.author.name}'

    def __str__(self):
        return f'{self.name} writen by {self.name} and published in {self.year}.'


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __repr__(self):
        return f'name:{self.name}, books:{len(self.books)}, authors:{len(self.authors)}'

    def __str__(self):
        return f'{self.name} keeps {len(self.books)} by {len(self.authors)} authors.'

    def new_book(self, name: str, year: int, author: Author):
        book = Book(name, year, author)

        self.books.append(book)
        author.add_book(book)
        if author not in self.authors:
            self.authors.append(author)

        return book

    def group_by_author(self, author: Author):
        result = [book.name for book in self.books if book.author == author]

        return result

    def group_by_year(self, year: int):
        result = [book.name for book in self.books if book.year == year]

        return result


john = Author('J.R.R. Tolkien', 'Orange Free State', '3 January')
joanne = Author('J. K. Rowling', 'England', '31 July')
british_library = Library('British Library')

british_library.new_book('The Hobbit', 1937, john)
british_library.new_book('The Lord of the Rings', 1954, john)
british_library.new_book('Harry Potter and the Philosopher\'s Stone', 1997, joanne)

assert john.__str__() == 'J.R.R. Tolkien was born on 3 January, Orange Free State. Write 2 book(s).'
assert british_library.__repr__() == 'name:British Library, books:3, authors:2'
assert british_library.group_by_author(john) == ['The Hobbit', 'The Lord of the Rings']
assert british_library.group_by_year(1997) == ['Harry Potter and the Philosopher\'s Stone']
