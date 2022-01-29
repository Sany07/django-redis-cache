from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import HttpResponse
from .models import BookList

@cache_page(60 * 15) # 60 sec * 15 min
def index(request):
    books = BookList.objects.all()
    context = {
        'books':books
    }
    return render(request,'home.html',context)

def book(request,id):
    if cache.get(id):
        book = cache.get(id)
    else:
        book = get_object_or_404(BookList,id = id)
        cache.set(id,book , 60 * 15)
    context = {
        'book':book
    }
    return render(request,'book.html',context)

def search(request):
    searchText = request.GET.get('text')
    if cache.get(searchText):
        books = cache.get(searchText)
    else:
        books = BookList.objects.filter(name__icontains = searchText ) | BookList.objects.filter(desc__icontains = searchText)
        cache.set(searchText,books , 60 * 15)
    context={
        'books':books
    }
    return render(request,'search.html',context)