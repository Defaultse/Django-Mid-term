from django.db import models
from django.utils import timezone
from utils.constants import BOOK_TYPE, BOOK_TYPE_BULLET


class BookJournalBase(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateField(default=timezone.now)


class Book(BookJournalBase):
    num_pages = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=30, null=True, blank=True)


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=BOOK_TYPE, default=BOOK_TYPE_BULLET),
    publisher = models.CharField(max_length=30, null=True, blank=True)