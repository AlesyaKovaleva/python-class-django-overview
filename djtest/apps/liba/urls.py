from django.urls import path

from . import views

urlpatterns = (
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('books/', views.ListView.as_view(), name='books_list'),
    path('book/<id>', views.BookView.as_view(), name='book_view'),
    path('authors/', views.AuthorsListView.as_view(), name='authors_list'),
    path('author/<id>', views.AuthorsView.as_view(), name='author_view'),
    path('publishers/', views.PublishersListView.as_view(), name='publisher_list'),
    path('publisher/<id>', views.PublishersView.as_view(), name='publisher_view'),
)
