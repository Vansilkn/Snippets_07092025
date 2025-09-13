from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    """ Получаем все элементы из базы данных. """
    snippets = Snippet.objects.all() 
    context = {
        'pagename':'Просмотр сниппетов',
        'snippets': snippets
    }
    return render(request, 'pages/view_snippets.html', context)


def get_snippets(request, snippet_id:int ):
    """ Получаем элемент по идентификатору из базы данных. """
    context = {'pagename':'Просмотр сниппета'}
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        return render(request, "pages/errors.html", {"errors": [f"""Сниппет с id={snippet_id} не найден"""]})
    else:
        context["snippet"] = snippet
        return render(request, "pages/snippet_page.html", context)
        