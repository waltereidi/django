from biblioteca.models.book import Book

def getIndex():
    books = getBooks()

    return { 'bookDataSource' : list(books)}

def getBooks():
    return Book.objects.all()

