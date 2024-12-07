from django import forms
from .models import Book


class BookForm(forms.Form):
    title = forms.CharField(max_length=200, label="Название книги")
    author = forms.CharField(max_length=100, label="Автор")
    publication_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        label="Дата публикации"
    )
    isbn = forms.CharField(max_length=13, label="ISBN")
    pages = forms.IntegerField(min_value=1, label="Количество страниц")



class BookFormModel(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'isbn', 'pages']
        labels = {
            'title': 'Название',
            'author': 'Автор',
            'publication_date': 'Дата публикации',
            'isbn': 'ISBN',
            'pages': 'Количество страниц',
        }
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
