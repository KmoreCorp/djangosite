from django.test import TestCase
from catalog.models import Author
# Create your tests here.

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Author.objects.create(first_name = 'Big', last_name = 'David')

    def test_first_name_lable(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').