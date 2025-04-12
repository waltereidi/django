from django.urls import path
from .controller.mainPageController import MainPageController

urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'),
    # path('', views.BibliotecaListView.as_view(), name='biblioteca_list'),
    path('<int:currentPage>/', MainPageController.index),
    # path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    # views.post_detail,
    # name='post_detail'),
]