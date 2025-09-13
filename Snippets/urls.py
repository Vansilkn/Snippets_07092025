from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views


urlpatterns = [
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="add_snippet"),
    path('snippets/list', views.snippets_page, name="snippets_list"),
    path('snippets/<int:snippet_id>/', views.get_snippets, name="snippet_detail"),
    path('snippets/create', views.create_snippets, name="create-snippet"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
