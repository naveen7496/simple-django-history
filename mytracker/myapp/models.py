from django.db import models
from simple_history.models import HistoricalRecords


class Author(models.Model):
    
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    changed_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

class Book(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    copies = models.PositiveIntegerField()
    category =  models.CharField(max_length=100)
    pages = models.PositiveIntegerField()
    number_of_chapters = models.PositiveIntegerField()
    changed_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value