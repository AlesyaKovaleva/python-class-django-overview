from django.contrib import admin
from . import models


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'pages')


class GenresAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


class PublishersAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CirculationsAdmin(admin.ModelAdmin):
    list_display = ('number', 'data_publish', 'book_id')


admin.site.register(models.Genre, GenresAdmin)
admin.site.register(models.Book, BooksAdmin)
admin.site.register(models.Author, AuthorsAdmin)
admin.site.register(models.Publisher, PublishersAdmin)
admin.site.register(models.Circulation, CirculationsAdmin)
