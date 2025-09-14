from django.http import Http404, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect, get_object_or_404
from MainApp.models import Snippet
from django.core.exceptions import ObjectDoesNotExist
from MainApp.forms import SnippetForm
from django.contrib import auth
from django.shortcuts import redirect



def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    # Создаем пустую форму при запросе GET
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)
    
    # Получае данные из формы и на их основе создаем новый сниппет, сохраняя его в БД
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("snippets_list") # URL для списка сниппитов 
        return render(request, "pages/add_snippet.html", context={"form": form})
    return HttpResponseNotAllowed(["POST"], "You must make POST request to add snippet.")


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


# Удаление данных из таблицы
def snippets_delete(request, snippet_id:int):
    """ Найти snippet по snippet_id или вернуть ошибку 404"""
    if request.method == "GET" or request.method == "POST":
        snippet = get_object_or_404(Snippet, id=snippet_id)
        snippet.delete()
    return redirect('snippets_list')


def snippets_edit(request, snippet_id:int):
    """ Редактирование сниппета """
    сontext = {'pagename': 'Обновление сниппета'}
    snippet = get_object_or_404(Snippet, id=snippet_id)

    # Создаем форму на основе данных snippets'а при запросе GET
    if request.method == "GET":
        form = SnippetForm(instance=snippet)
        return render(request, 'pages/add_snippet.html', сontext | {"form": form})
    
    # Получае данные из формы и на их основе обновляем сниппет, сохраняя его в БД
    if request.method == "POST":
        data_form = request.POST
        snippet.name = data_form["name"]
        snippet.lang = data_form["lang"]
        snippet.code = data_form["code"]
        snippet.save()
        return redirect("snippets_list") # URL для списка сниппитов 


def login(request):
   if request.method == 'POST':
       username = request.POST.get("username")
       password = request.POST.get("password")
       # print("username =", username)
       # print("password =", password)
       user = auth.authenticate(request, username=username, password=password)
       if user is not None:
           auth.login(request, user)
       else:
           # Return error message
           pass
   return redirect(to='home')


def logout(request):
    auth.logout(request)
    return redirect(to='home')
