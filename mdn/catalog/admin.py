from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language
# Register your models here.
class BooksInline(admin.TabularInline):
    """docstring for BooksInline"""
    model = Book
    extra = 0


admin
class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ('first_name', 'last_name', ('date_of_birth', 'date_of_death'))
    inlines = [BooksInline]

class BooksInstanceInline(admin.TabularInline):
    """docstring for BooksInstanceInline"""
    model = BookInstance
    #不显示多余空行
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """docstring for BookAdmin"""
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """docstring for BookInstanceAdmin"""
    list_display = ('book','status','due_back','id')
    list_filter = ('status', 'due_back')
    fieldsets = [
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    ]



# admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author, AuthorAdmin)
# admin.site.register(BookInstance,BookInstanceAdmin)
# admin.site.register(Language)