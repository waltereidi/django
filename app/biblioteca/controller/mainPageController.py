from django.shortcuts import render
from biblioteca.models.book import  Book
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.core.paginator import   Paginator, EmptyPage,\
                                    PageNotAnInteger

from biblioteca.service.mainPageService import MainPageService

class MainPageController:
    
                                        
    def index(request):
        # View code here...
        t = loader.get_template("biblioteca/view/bookContainer.html")
        currentPage = int(request.GET.get('currentPage' , '0'))
        categories = str(request.GET.get('categories','')).split(',')
        
        return HttpResponse(t.render(MainPageService.getIndex(currentPage,categories), request))




