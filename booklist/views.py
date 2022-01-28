from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from .models import BookList

from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT


CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

@cache_page(60 * 15)
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
        cache.set(id,book )
    context = {
        'book':book
    }
    return render(request,'book.html',context)
