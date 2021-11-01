from django.urls import path
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/Hebrew', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book/Japanese', views.BokListView.as_view(), name='book'),
    path('bok/<int:pk>', views.BokDetailView.as_view(), name='book-detail'),
    path('bks/', views.BkListView.as_view(), name='bks'),
    path('bK/<int:pk>', views.BkDetailView.as_view(), name='book-detail'),
    path('contact', views.ContactView.as_view(), name='contact'),
    path('authors/English', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:id>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),

]