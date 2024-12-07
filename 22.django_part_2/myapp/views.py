from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm, BookFormModel


def index(request):
    books = Book.objects.all()  
    paginator = Paginator(books, 1) 

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})


def add_book_form_view(request):
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
            return redirect('books')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})


def add_book_form_model_view(request):
    if request.method == 'POST':
        form = BookFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookFormModel()

    return render(request, 'add_book.html', {'form': form})