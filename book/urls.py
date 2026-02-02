from . import views
from django.urls import path

urlpatterns = [
    # path('book/', views.index_view,),
    path('book/', views.book_list_view),
    path('book/<int:id>/', views.book_detail_view),

]