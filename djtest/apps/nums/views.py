from django.shortcuts import render

from .models import Number


NOT_FOUND_TEMPLATE = 'nums/404.html'


def list_view(request):
    numbers = Number.objects.all()
    return render(request, 'nums/list.html', context={'numbers': numbers})


def create_view(request, number):
    number = Number(value=number)
    number.save()

    return render(request, 'nums/created.html', context={'number': number})


def update_view(request, number_id, value):
    try:
        number = Number.objects.get(id=number_id)
    except Number.DoesNotExist:
        return render(request, NOT_FOUND_TEMPLATE, context={'number_id': number_id})

    number.value = value
    number.save()

    return render(request, 'nums/updated.html', context={'number': number})


def delete_view(request, number_id):
    template = 'nums/deleted.html'

    try:
        Number.objects.get(id=number_id).delete()
    except Number.DoesNotExist:
        template = NOT_FOUND_TEMPLATE

    return render(request, template, context={'number_id': number_id})
