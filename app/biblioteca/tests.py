from django.test import TestCase

# Create your tests here.
from biblioteca.service.mainPageService import MainPageService
from biblioteca.models.book import Book

class AnimalTestCase(TestCase):
    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        
        
        result =  MainPageService.getCategoriesBookCount
        print(result)
        self.assertIsNotNone(result)