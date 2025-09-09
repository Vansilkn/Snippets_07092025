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
    ls_snippets = Snippet.objects.all()
    context = {'ls_snippets': ls_snippets}
    return render(request, 'pages/view_snippets.html', context)


def get_snippets(request, snippets_id:int ):
    """ Получаем элемент по идентификатору из базы данных. """
    try:
        snippets = Snippet.objects.get(id=snippets_id)
    except ObjectDoesNotExist:
        return render(request, "00000.html", {"errors": [f"""Сниппет с id={snippets_id} не найден"""]})
    else:
        context = {"snippets": snippets} 
        return render(request, "pages/snippet_page.html", context)