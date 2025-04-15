class PaginationDAO:
    currentPage = 0
    totalCount = 0 
    paginationSize = 0 
    def __init__(self,currentPage:int , totalCount:int , paginationSize:int):
        self.currentPage = currentPage
        self.totalCount = totalCount 
        self.paginationSize = paginationSize
        
        pass
    
    def getPaginationArray(self ):
        
        if( self.paginationSize > self.totalCount):
            pagination = list()
            pagination.append({'page' : 1 , 'selected' : True , 'pageLink':'#' })
            return {
            'pagination' : pagination, 
            'totalCount' : self.totalCount ,
            'paginationSize':self.paginationSize,
            'nextPage' : '#',
            'previousPage':'#',
            'previousPageButtonStyle':'disabled',
            'nextPageButtonStyle':'disabled'
            }

        
        pages = self.totalCount/self.paginationSize

        pagination = list()
        count = 0
        
        while(count < pages):
            pagination.append({'page' : count+1 , 
                               'selected' : count+1 == self.currentPage ,
                               'pageLink' : '?currentPage='+str(count+1)
                               })
            count += 1
        
        return {
            'pagination' :pagination , 
            'totalCount' : self.totalCount ,
            'paginationSize':self.paginationSize,
            'nextPage' : '?currentPage='+str(self.currentPage+1) if self.currentPage < self.totalCount else '#',
            'previousPage': '?currentPage='+str(self.currentPage-1) if self.currentPage > 1 else '#',
            'previousPageButtonStyle':'disabled' if self.currentPage < self.totalCount else  '?currentPage='+str(self.currentPage-1),
            'nextPageButtonStyle':'disabled' if '?currentPage='+str(self.currentPage+1) else '?currentPage='+str(self.currentPage+1)
            }
        
            
        