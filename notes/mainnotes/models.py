from django.db import models
from django.urls import reverse


class Note(models.Model):
    title = models.CharField('Название', max_length=20)
    text = models.TextField('Запись', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note')