from django.test import TestCase
from biblioteca.componentsDAO.paginationDAO import PaginationDAO 

class PaginationTest(TestCase):
    def test_pagination(self):
        pagination = PaginationDAO(1 , 10 , 5)
        
        result = pagination.getPaginationArray()
        self.assertTrue(len(result) == 2)
        