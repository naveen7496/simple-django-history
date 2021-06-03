from django.contrib import admin
from . models import Author, Book
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(Author, SimpleHistoryAdmin)
admin.site.register(Book, SimpleHistoryAdmin)

