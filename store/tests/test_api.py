from django.urls import reverse
from rest_framework.test import APITestCase

from store.models import Book


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='Test book', price=25)
        book_2 = Book.objects.create(name='Test book 2', price=28)
        url = reverse('book-list')
        print(url)
        response = self.client.get(url)
        
