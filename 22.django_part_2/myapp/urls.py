from django.urls import path
from .views import index, add_book_form_view, add_book_form_model_view

urlpatterns = [
    path('', index, name='books'),
    path('add_book_form', add_book_form_view, name='add_book_form'),
    path('add_book_form_model', add_book_form_model_view, name='add_book_form_model')
]