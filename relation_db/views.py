from django.shortcuts import render
from . import models
# Create your views here.

def relation_db(request):
    if request.method == 'GET':
        userr = models.Person.objects.all()
    
    return render(
        request,
        'relation_db.html',
        {
            'userr' : userr
        }
    )