from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views import View
from . models import Book, Author
from django.contrib.auth.models import User

class BookListView(ListView):
    model = Book

class BookDetailView(DetailView):
    model = Book

class AuthorListView(ListView):
    model = Author

class AuthorDetailView(DetailView):
    model = Author

class BookHistory(View):

    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        history_book_objects = book.history.all()
        context = {
            'all_objects' : []
        }
        
        for i in range(len(history_book_objects)):
            object_and_changes = {}
            if i == len(history_book_objects)-1:
                object_and_changes['object'] = history_book_objects[i]
                object_and_changes['history_changes'] = None

            else:
                new_history = history_book_objects[i]
                old_history = history_book_objects[i+1]
                delta = new_history.diff_against(old_history)
                changed_objects = delta.changes
                object_and_changes['object'] = history_book_objects[i]
                object_and_changes['history_changes'] = changed_objects
                remove = False
                changed_by_object = None
                if len(changed_objects) > 0:
                    for current_change in changed_objects:
                        if current_change.field == 'changed_by':
                            changed_by_object = current_change
                            remove = True
                if remove == True:
                    changed_objects.remove(changed_by_object)
            
            context['all_objects'].append(object_and_changes)
            
        return render(request, 'myapp/history_books.html', context)

class AuthorHistory(View):

    def get(self, request, pk):
        author = Author.objects.get(id=pk)
        history_author_objects = author.history.all()
        context = {
            'all_objects' : []
        }
        
        for i in range(len(history_author_objects)-1):
            object_and_changes = {}
            new_history = history_author_objects[i]
            old_history = history_author_objects[i+1]
            delta = new_history.diff_against(old_history)
            changed_objects = delta.changes
            object_and_changes['object'] = history_author_objects[i]
            object_and_changes['history_changes'] = changed_objects
            remove = False
            changed_by_object = None
            if len(changed_objects) > 0:
                for current_change in changed_objects:
                    if current_change.field == 'changed_by':
                        changed_by_object = current_change
                        remove = True
            if remove == True:
                changed_objects.remove(changed_by_object)
            
            context['all_objects'].append(object_and_changes)
        return render(request, 'myapp/history_authors.html', context)

class HistoryDetailView(View):

    def get(self, request, pk):
        history_object = Book.history.get(history_id=pk)
        if history_object.changed_by_id:
            user = User.objects.get(id=history_object.changed_by_id)
            context={
                'history_object':history_object,
                'user' : user
            }
        else:
            context={
                'history_object':history_object
            }


        return render(request, 'myapp/history_book_detail.html', context)

class AuthorHistoryDetailView(View):

    def get(self, request, pk):
        history_object = Author.history.get(history_id=pk)
        if history_object.changed_by_id:
            user = User.objects.get(id=history_object.changed_by_id)
            context={
                'history_object':history_object,
                'user' : user
            }
        else:
            context={
                'history_object':history_object
            }


        return render(request, 'myapp/history_author_detail.html', context)


def revertObject(request, slug):
    object_type = slug.split("-")[0]
    pk = slug.split("-")[1]
    if object_type == 'book':
        history_object = Book.history.get(history_id=pk)
    else:
        history_object = Author.history.get(history_id=pk)
    history_object.changed_by = request.user
    history_object.instance.save()
    return redirect(f'/{object_type}s/')

class UserList(ListView):
    model = User

def listHistoryByUser(request, pk):
    book_history_list = Book.history.filter(changed_by_id=pk)
    author_history_list = Author.history.filter(changed_by_id=pk)
    context = {
        "book_history_list" : book_history_list,
        "author_history_list" : author_history_list

    }
    return render(request, 'myapp/history_by_user.html', context)