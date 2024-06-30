from django.test import TestCase
from .models import Author
# unittest

class AuthorTestCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name = "Akira")
        
    def test_is_correct_instance(self):
        self.assertIsInstance(self.author, Author)
        
    def test_exists(self):
        author = Author.objects.get(pk = 1)
        self.assertTrue(author)