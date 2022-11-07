from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg


# Create your views here.
def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating")) 
    return render(request, "book_outlet/index.html",{
        "books":books,
        "total_num_of_books":num_books,
        "avg_rating":avg_rating,
    })

def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id) 
    # except:
    #     raise Http404()   es sab ki jagah
    book = get_object_or_404(Book, slug=slug)  # throw 404 if book is not found
    return render(request, "book_outlet/book_detail.html",{
        "title":book.title,
        "author":book.authors,
        "rating":book.rating,
        "is_bestselling":book.is_bestselling
    }) 