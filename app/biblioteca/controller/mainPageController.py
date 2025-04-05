from django.shortcuts import render
from biblioteca.models.book import  Book
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.core.paginator import   Paginator, EmptyPage,\
                                    PageNotAnInteger

from biblioteca.service import mainPageService as service
                                    
def index(request):
    # View code here...
    t = loader.get_template("biblioteca/view/mainPage.html")
    c = service.getIndex()
    return HttpResponse(t.render(c, request))




