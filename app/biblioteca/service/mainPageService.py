from biblioteca.models.book import Book
from biblioteca.models.categoryBook import CategoryBook
from django.db.models import Count

class MainPageService():
    
    def getIndex():
        return { 
                'bookDataSource' : list(MainPageService.getBooks()),
                'categoryBookDataSource' : list(MainPageService.getCategoriesBookCount())
                }

    def getBooks():
        return Book.objects.all()

    def getCategoriesBookCount() :
        result =CategoryBook.objects.values('category__name').annotate(total=Count('id'))
        
        return list(result)

