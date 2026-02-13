from . import views
from django.urls import path

urlpatterns = [
    # path('book/', views.index_view,),
    path('book/', views.book_list_view),
    path('book/<int:id>/', views.book_detail_view),
    path('book/<int:id>/delete/', views.delete_book_view),
    path('book/<int:id>/update/', views.update_book_view),

    path("create_book/", views.create_book_view)
]