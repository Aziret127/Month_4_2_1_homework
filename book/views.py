from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse  
from . import models



# Create your views here.


# View for the /book/ URL
# def index_view(request):
#    if request.method == "GET":
#          return HttpResponse("Жизнь - это то, что с тобой происходит, пока ты строишь планы.")
   

def book_detail_view(request, id):
    if request.method == "GET":
        book_id = get_object_or_404(models.Book, id=id)
        return render(
            request,
            "book_detail.html",
            {
                "book_id": book_id,
            },
        )
    

def book_list_view(request):
    if request.method == "GET":
        book = models.Book.objects.all()
        return render(
            request,
            "book.html",
            {
                "book": book,
            },
        )