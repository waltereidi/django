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
            return list({'page' : 1 , 'selected' : True })

        pages = self.paginationSize/self.totalCount
        
        result = list()
        count = 0
        
        while(count < pages):
            page =result.append({'page' : count+1 , 'selected' : count+1 == self.currentPage })
            count += 1
        
        return result
        
            
        