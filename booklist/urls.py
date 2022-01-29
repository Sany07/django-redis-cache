
from django.urls import path,include
from booklist.views import index, book, search

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/',book , name='book'),
    path('search/', search , name='search-recipe'),
    

]
