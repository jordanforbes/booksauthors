from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('makenewbook',views.createBook),
    path('book/<bookId>', views.showBook)
]