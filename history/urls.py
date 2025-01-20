from django.urls import path

from history import views

app_name = 'history'

urlpatterns = [
    path('history/', views.history, name='history'),
    path('history/review/', views.review, name='review')
]