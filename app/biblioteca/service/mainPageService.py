from biblioteca.models.book import Book
from biblioteca.models.categoryBook import CategoryBook
from django.db.models import Count


class MainPageService():
    
    def getIndex(currentPage:int):
        
        result = { 
                'bookDataSource' : list(MainPageService.getBooks(currentPage)),
                'categoryBookDataSource' : list(MainPageService.getCategoriesBookCount())
                
                }
        return result
    
    def getPaginationConfig() -> int :
        return 5
    
    def getBooks(currentPage:int):
        return MainPageService.getBooksProjection().all()[currentPage:MainPageService.getPaginationConfig]
    
    def getBooksProjection():
        return Book.objects.filter(book__active=1)
    
    def getBookCount():
        return MainPageService.getBooksProjection().count()
    
#all()[currentPage:MainPageService.getPaginationConfig]
    def getCategoriesBookCount():
        result =CategoryBook.objects.values('category__name').annotate(total=Count('id'))
        
        return list(result)
        
    

