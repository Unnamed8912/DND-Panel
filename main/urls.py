from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.characters, name='characters'),
    path('characters/create', views.create, name='create'),
    path('characters/<slug:slug>/', views.display_character, name='display_character'),
    path('characters/<slug:slug>/rename/', views.rename_character, name='rename_character'),
]