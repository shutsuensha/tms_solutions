from django.shortcuts import render
from .forms import BookForm
from .models import Book

def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                publication_date=form.cleaned_data['publication_date'],
                isbn=form.cleaned_data['isbn'],
                pages=form.cleaned_data['pages']
            )
    else:
        form = BookForm()
    return render(request, 'index.html', {'form': form})