from biblioteca.models.book import Book
from biblioteca.models.categoryBook import CategoryBook
from django.db.models import Count
from biblioteca.componentsDAO.paginationDAO import PaginationDAO

class MainPageService:
    
    def getIndex(currentPage:int ):
        
        result = { 
                    'bookDataSource' : list(MainPageService.getBooks(currentPage)),
                    'categoryBookDataSource' : list(MainPageService.getCategoriesBookCount()),
                    'paginationDataSource' : MainPageService.getPagination(currentPage)
                }
        return result
    
    def getPagination(currentPage:int ) -> PaginationDAO : 
        paginationSize = MainPageService.getPaginationSize()
        totalCount = MainPageService.getBookCount()
        dao =  PaginationDAO(
            currentPage,  
            totalCount,
            paginationSize
        )
        return dao.getPaginationArray()
    
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
        
    

