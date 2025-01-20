from django.urls import path

from fighting import views

app_name = 'fighting'

urlpatterns = [
    path('fighting/', views.fighting, name='fighting'),
    path('fighting/current_fight/', views.current_fight)
]