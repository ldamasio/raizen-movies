from django.contrib import admin
from django.urls import path
from movies_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', views.FilmListView.as_view(), name='film-list'),
]
