from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_year = models.DateField()
    birth_country = models.CharField(max_length=255)

    def get_books(self):
        return self.books.all()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name,)


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255)
    author_id = models.ManyToManyField(Author, related_name='publishers')

    def __str__(self):
        return '%s' % self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s' % self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    pages = models.IntegerField()
    created_at = models.DateField()
    author_id = models.ManyToManyField(Author, default=None, related_name='books', null=True, blank=True)
    publisher_id = models.ForeignKey(Publisher, default=None, related_name='book', on_delete=models.SET_NULL, null=True)

    def authors(self):
        return [author for author in self.author_id.all()]

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)
        publisher = self.publisher_id
        for author in self.author_id.all():
            publisher.author_id.add(author)

    def __str__(self):
        return '%s' % self.title


class Circulation(models.Model):
    number = models.IntegerField()
    data_publish = models.DateField()
    publisher_id = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    book_id = models.ForeignKey(Book, related_name='circulation', on_delete=models.CASCADE)

    def __str__(self):
        return '%s pages, %s' % (self.number, self.data_publish)
