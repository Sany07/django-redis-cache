
from django.urls import path,include
from booklist.views import index, book

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/',book , name='book'),

]
