from django.shortcuts import render
from biblioteca.models.book import  Book
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.core.paginator import   Paginator, EmptyPage,\
                                    PageNotAnInteger

from biblioteca.service.mainPageService import MainPageService

class MainPageController():
    
                                        
    def index(request,currentPage:int):
        # View code here...
        t = loader.get_template("biblioteca/view/bookContainer.html")
        
        return HttpResponse(t.render(MainPageService.getIndex(currentPage), request))




