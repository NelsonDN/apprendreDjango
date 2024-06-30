from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields = ['title', 'author', 'quantity']
    fieldsets = [
        ('Informatios manga', {'fields': ['title', 'author'] }),
        ('Informations magasin', {'fields': ['quantity']})
    ]
    
    list_display = ('title', 'author', 'quantity')
    list_filter = ['title', 'author']
    search_fields = ['title', 'author__name']
    list_per_page = 10
    
    
#admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book, BookAdmin)
