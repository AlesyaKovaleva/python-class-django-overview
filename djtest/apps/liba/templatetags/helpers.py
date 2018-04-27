from django import template

register = template.Library()


@register.filter
def get_author_books_by_publisher(author, publisher):
    return author.books.filter(publisher_id=publisher)
