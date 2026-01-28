from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_view(request):
   if request.method == "GET":
         return HttpResponse("Жизнь - это то, что с тобой происходит, пока ты строишь планы.")
