# from django.http.response import HttpResponse
# from django.shortcuts import redirect, render
# from django.views.generic import ListView, DetailView
# from django.views import View
# from . models import Book, Author
# from django.contrib.auth.models import User

# class BookListView(ListView):
#     model = Book

# class BookDetailView(DetailView):
#     model = Book

# class AuthorListView(ListView):
#     model = Author

# class AuthorDetailView(DetailView):
#     model = Author

# class BookHistory(View):

#     def get(self, request, pk):
#         book = Book.objects.get(id=pk)
#         history_book_objects = book.history.all()
#         context = {
#             'history_book_objects' : history_book_objects,
#         }
        
#         return render(request, 'myapp/history_books.html', context)

# class AuthorHistory(View):

#     def get(self, request, pk):
#         author = Author.objects.get(id=pk)
#         history_author_objects = author.history.all()
#         context = {
#             'history_author_objects' : history_author_objects,
#         }
        
#         return render(request, 'myapp/history_authors.html', context)

# class HistoryDetailView(View):

#     def get(self, request, pk):
#         history_object = Book.history.get(history_id=pk)
#         if history_object.changed_by_id:
#             user = User.objects.get(id=history_object.changed_by_id)
#             context={
#                 'history_object':history_object,
#                 'user' : user
#             }
#         else:
#             context={
#                 'history_object':history_object
#             }


#         return render(request, 'myapp/history_book_detail.html', context)

# class AuthorHistoryDetailView(View):

#     def get(self, request, pk):
#         history_object = Author.history.get(history_id=pk)
#         if history_object.changed_by_id:
#             user = User.objects.get(id=history_object.changed_by_id)
#             context={
#                 'history_object':history_object,
#                 'user' : user
#             }
#         else:
#             context={
#                 'history_object':history_object
#             }


#         return render(request, 'myapp/history_author_detail.html', context)


# def revertObject(request, slug):
#     object_type = slug.split("-")[0]
#     pk = slug.split("-")[1]
#     if object_type == 'book':
#         history_object = Book.history.get(history_id=pk)
#     else:
#         history_object = Author.history.get(history_id=pk)
#     history_object.changed_by = request.user
#     history_object.instance.save()
#     return redirect(f'/{object_type}s/')

# class UserList(ListView):
#     model = User

# def listHistoryByUser(request, pk):
#     book_history_list = Book.history.filter(changed_by_id=pk)
#     author_history_list = Author.history.filter(changed_by_id=pk)
#     context = {
#         "book_history_list" : book_history_list,
#         "author_history_list" : author_history_list

#     }
#     return render(request, 'myapp/history_by_user.html', context)


# {%  extends 'base.html'%}


# {% block content %}
#     {% for author_object in history_author_objects %}
            
#     <a href="{% url 'author-history-details' author_object.history_id %}">{{author_object.name}}<br></a>
#     {{author_object.subject}}<br><br>

#     {% endfor %}
# {% endblock %}