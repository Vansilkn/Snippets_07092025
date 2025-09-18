from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name="home"),
    path('snippets/add', views.add_snippet_page, name="add_snippet"),
    path('snippets/list', views.snippets_page, name="snippets_list"),
    path('snippets/my', views.my_snippets, name="my-snippets"),
    path('snippets/<int:snippet_id>/', views.get_snippets, name="snippet_detail"),
    path('snippets/<int:snippet_id>/delete', views.snippets_delete, name="snippet-delete"),
    path('snippets/<int:snippet_id>/edit', views.snippets_edit, name="snippet-edit"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.create_user, name='register'),
    path('comment/add', views.comment_add, name="comment_add"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
