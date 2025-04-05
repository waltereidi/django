from biblioteca.models.book import Book

def getIndex():
    object_list = Book.objects.all()

    return { 'foo' : list(object_list).pop().title}

