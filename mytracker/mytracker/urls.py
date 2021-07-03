
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('book_history/<int:pk>', views.BookHistory.as_view(), name='book-history'),
    path('book_history_details/<int:pk>', views.HistoryDetailView.as_view(), name='book-history-details'),
    path('revert/<slug>', views.revertObject, name='revert'),
    path('users/', views.UserList.as_view(), name='users'),
    path('history_by_user/<int:pk>', views.listHistoryByUser, name='userhistorylist'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('author_history/<int:pk>', views.AuthorHistory.as_view(), name='author-history'),
    path('author_history_details/<int:pk>', views.AuthorHistoryDetailView.as_view(), name='author-history-details'),

]
