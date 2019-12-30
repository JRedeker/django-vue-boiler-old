
from django.urls import path

from . import views

app_name = 'todo_app'
urlpatterns = [
    # ex: /
    path('', views.HomePageView.as_view(), name='Home'),
]