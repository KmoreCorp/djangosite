from django.db import models
from django.urls import reverse 
import uuid
# Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Genre(models.Model):
    name = models.CharField(help_text='Enter a book genre (e.g. Science Fiction)', \
        max_length=50)
    
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"



    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField( max_length=50)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000,\
        help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, \
        help_text= '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    
    ## 为了显示genre，many2many field
    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'    

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, \
        help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete = models.SET_NULL, null=True, blank=True)
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    

    LOAN_STATUS=(
        ('m','维护中'),
        ('o', '已借出'),
        ('a', '可借阅'),
        ('r', '已预定'),
        )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default = 'm',
        help_text='Book availability'
        )
    class Meta:
        verbose_name = "Book Instance"
        verbose_name_plural = "Book Instances"
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)

    def __str__(self):
        return f'{self.id} ({self.book.title})'
    
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)


    class Meta:
        verbose_name = "作者"
        verbose_name_plural = "作者"
        ordering = ['last_name', 'first_name']
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

class Language(models.Model):
    language = models.CharField(max_length=200,\
        help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return self.language
    