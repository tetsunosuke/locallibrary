from django.contrib import admin
from .models import Author,Genre, Book,BookInstance, Language

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]


    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    display_genre.short_description = 'Genre'


#class BookInstanceAdmin(admin.ModelAdmin):
    #list_filter = ('status', 'due_back')

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )


class LanguageAdmin(admin.ModelAdmin):
    list_filter = ('Hebrew', 'Japanese','English')


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Language)
#admin.site.register(BookInstance)
