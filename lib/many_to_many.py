class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str) or not title.strip():
            raise Exception("Title must be a non-empty string")
        self.title = title
        Book.all.append(self)

    # Return all contracts for this book
    def contracts(self):
        return [c for c in Contract.all if c.book == self]

    # Return all authors for this book via contracts
    def authors(self):
        return [c.author for c in self.contracts()]


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Name must be a non-empty string")
        self.name = name
        Author.all.append(self)

    # Return all contracts for this author
    def contracts(self):
        return [c for c in Contract.all if c.author == self]

    # Return all books for this author via contracts
    def books(self):
        return [c.book for c in self.contracts()]

    # Sign a new contract with a book
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str) or not date.strip():
            raise Exception("date must be a non-empty string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("royalties must be a non-negative integer")
        return Contract(self, book, date, royalties)

    # Compute total royalties from all contracts
    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str) or not date.strip():
            raise Exception("date must be a non-empty string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("royalties must be a non-negative integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    # Class method to find all contracts by a given date
    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]
