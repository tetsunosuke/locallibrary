from django.shortcuts import render
from .models import Book, Author, BookInstance
from django.views import generic
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from . import forms


class ContactView(generic.FormView):
   template_name = "catalog/contact.html"
   form_class = forms.InquiryForm
   success_url = reverse_lazy('contact')

   def form_valid(self, form):
       form.send_email()
       return super().form_valid(form)





class BookCreate(PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']
    permission_required = 'catalog.can_mark_returned'


class BookUpdate(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'summary', 'isbn', 'genre', 'language']
    permission_required = 'catalog.can_mark_returned'


class BookDelete(PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    permission_required = 'catalog.can_mark_returned'



class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}
    permission_required = 'catalog.can_mark_returned'


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('authors')
    permission_required = 'catalog.can_mark_returned'




def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    template_name = "catalog/book_list.html"
    queryset = Book.objects.filter(language__name__icontains='Hebrew')

class BookDetailView(generic.ListView):
    model = Book


class BokListView(generic.ListView):
    model = Book
    template_name = "catalog/bok_list.html"
    queryset = Book.objects.filter(language__name__icontains='Japanese')


class BokDetailView(generic.ListView):
    model = Book
    def get_queryset(self):
        self.book.summary = get_object_or_404(Book, summary=self.kwargs['summary'])
        return Book.objects.filter(book=self.book.summary)




class BkListView(generic.ListView):
    model = Book
    template_name = "catalog/bk_list.html"
    queryset = Book.objects.filter(language__name__icontains='English')

class BkDetailView(generic.ListView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.ListView):
    model = Author
