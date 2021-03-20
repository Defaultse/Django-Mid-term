from django.urls import path
from api.views import *

urlpatterns = [
    path('books/', BookViewSet.as_view({'get': 'book'})),
    path('journals/', JournalViewSet.as_view({'get': 'journal'}))
]