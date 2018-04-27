from django.shortcuts import render
from django.views import View
from .models import Book, Author, Publisher

NOT_FOUND_TEMPLATE = 'liba/oops/404.html'


class ListView(View):
    def get(self, request):
        books = Book.objects.all().prefetch_related('author_id')
        return render(request, 'liba/list.html', context={'books': books})


class BookView(View):
    def get(self, request, *args, **kwargs):
        book_id = kwargs['id']
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return render(request, NOT_FOUND_TEMPLATE)

        return render(request, 'liba/book.html', context={'book': book})


class AuthorsListView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'liba/authors.html', context={'authors': authors})


class AuthorsView(View):
    def get(self, request, *args, **kwargs):
        author_id = kwargs['id']
        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return render(request, NOT_FOUND_TEMPLATE)
        return render(request, 'liba/author.html', context={'author': author})


class PublishersListView(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        return render(request, 'liba/publishers.html', context={'publishers': publishers})


class PublishersView(View):
    def get(self, request, *args, **kwargs):
        publisher_id = kwargs['id']
        try:
            publisher = Publisher.objects.get(id=publisher_id)
        except Publisher.DoesNotExist:
            return render(request, NOT_FOUND_TEMPLATE)

        authors = publisher.author_id.all()
        books = {}
        for author in authors:
            books[author] = author.books.filter(publisher_id=publisher)

        return render(request, 'liba/publisher.html', context={'publisher': publisher, 'books': books})


class MenuView(View):
    def get(self, request):
        return render(request, 'liba/menu.html')
