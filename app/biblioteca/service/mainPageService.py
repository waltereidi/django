from biblioteca.models.book import Book
from biblioteca.models.categoryBook import CategoryBook
from django.db.models import Count
from biblioteca.componentsDAO.paginationDAO import PaginationDAO
from django.db.models import Q

class MainPageService:
    
    def getIndex(currentPage:int ,categories:list):
        
        result = { 
                    'bookDataSource' : list(MainPageService.getBooks(currentPage , categories)),
                    'categoryBookDataSource' : list(MainPageService.getCategoriesBookCount()),
                    'paginationDataSource' : MainPageService.getPagination(currentPage, categories)
                }
        return result
    
    def getPagination(currentPage:int , categories:list ) -> PaginationDAO : 
        paginationSize = MainPageService.getPaginationSize()
        totalCount = MainPageService.getBookCount(categories)
        dao =  PaginationDAO(
            currentPage,  
            totalCount,
            paginationSize
        )
        return dao.getPaginationArray()
    
    def getPaginationSize() -> int :
        return 5
    
    def getBooks(currentPage:int , categories:list ):
        maxPages = MainPageService.getPaginationSize()
        projection = MainPageService.getBooksProjection(categories)
        
        return projection.all()[currentPage:maxPages]

    def getBooksProjection(categories:list):
        result = Book.objects.filter( active = 1)
        
        if(categories[0] != ''):
            result.filter(category__name__in = categories)    
            
        return result
    
    def getBookCount(categories:list):
        projection = MainPageService.getBooksProjection(categories)
        
        return projection.count()
    
#all()[currentPage:MainPageService.getPaginationConfig]
    def getCategoriesBookCount():
        result =CategoryBook.objects.values('category__name').annotate(total=Count('id'))
        
        return list(result)
        
    

