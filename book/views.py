from django.shortcuts import redirect,render, get_object_or_404
# from django.http import HttpResponse  
from . import models, forms

#UPDATE
def update_book_view(request,id):
    book_id = get_object_or_404(models.Book, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        if form.is_valid():
            form.save()
            return redirect('/book/')
    else:
        form = forms.BookForm(instance=book_id)
    return render(
        request,
        'update_book.html',
        {
            "form": form,
            "book_id": book_id
        }
    )

#DELETE
def delete_book_view(request, id):
    book_id = get_object_or_404(models.book, id=id)
    book_id.delete()
    return redirect('/book/')

#CREATE BOOK
def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/book/')
    else:
        form = forms.BookForm()
        return render(
            request,
            'create_book_html',
            {
                "form": form
            }
        )


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
# Create your views here.


# View for the /book/ URL
# def index_view(request):
#    if request.method == "GET":
#          return HttpResponse("Жизнь - это то, что с тобой происходит, пока ты строишь планы.")
   