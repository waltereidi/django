from django.shortcuts import render
from biblioteca.models.book import  Book
from django.http import HttpResponse
from django.template import loader
# Create your views here.
from django.core.paginator import   Paginator, EmptyPage,\
                                    PageNotAnInteger
                                    

def biblioteca_list(request):
    # View code here...
    t = loader.get_template("biblioteca/base.html")
    c = {"foo": "bar"}
    return HttpResponse(t.render(c, request), content_type="application/xhtml+xml")

