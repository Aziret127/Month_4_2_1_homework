from django.urls import path
from . import views

urlpatterns = [
    path('all_userr/', views.relation_db),
    
]