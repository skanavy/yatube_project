# ice_cream/views.py
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)


def group_posts(request, pk):
    return HttpResponse(f'slug {pk}')
