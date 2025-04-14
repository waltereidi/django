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
            pagination.append({'page' : 1 , 'selected' : True })
            return {
            'pagination' : pagination, 
            'totalCount' : self.totalCount ,
            'paginationSize':self.paginationSize
            }

        
        pages = self.totalCount/self.paginationSize

        pagination = list()
        count = 0
        
        while(count < pages):
            pagination.append({'page' : count+1 , 'selected' : count+1 == self.currentPage })
            count += 1
        
        return {
            'pagination' :pagination , 
            'totalCount' : self.totalCount ,
            'paginationSize':self.paginationSize
            }
        
            
        