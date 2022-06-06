from django.urls import path
from . import views
from .views import BooksView

urlpatterns = [
    path('', BooksView.as_view()),
]