from biblioteca.models.book import Book
from biblioteca.models.categoryBook import CategoryBook
from django.db.models import Count


class MainPageService:
    
    def getIndex(currentPage:int ):
        
        result = { 
                    'bookDataSource' : list(MainPageService.getBooks(currentPage)),
                    'categoryBookDataSource' : list(MainPageService.getCategoriesBookCount()),
                    'totalCount' : MainPageService.getBookCount() ,
                    'paginationSize' : MainPageService.getPaginationSize() ,
                }
        return result
    
    def getPaginationSize() -> int :
        return 5
    
    def getBooks(currentPage:int):
        maxPages = MainPageService.getPaginationSize()
        
        return Book.objects.all()[currentPage:maxPages]
    
    def getBookCount():
        return Book.objects.count()
    
#all()[currentPage:MainPageService.getPaginationConfig]
    def getCategoriesBookCount():
        result =CategoryBook.objects.values('category__name').annotate(total=Count('id'))
        
        return list(result)
        
    

