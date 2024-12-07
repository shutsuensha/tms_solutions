from django import forms

class BookForm(forms.Form):
    title = forms.CharField(max_length=200, label="Название книги")
    author = forms.CharField(max_length=100, label="Автор")
    publication_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        label="Дата публикации"
    )
    isbn = forms.CharField(max_length=13, label="ISBN")
    pages = forms.IntegerField(min_value=1, label="Количество страниц")