from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView
from .models import Book
from django.views import View
from .forms import BookForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.
class CreateBookView(View):
    def get(self, request):  
        form = BookForm()
        return render(request, "rental/create.html", {
            "form": form
        })
    
    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home")
            
        return render(request, "rental/create.html", {
            "form": form
        })
        

class HomeView(TemplateView):
    template_name = "rental/home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        context["books"] = books
        return context
    
class DetailedBookView(DetailView):
    template_name = "rental/single_book.html"
    model = Book
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def editBook(request, id):
    data = Book.objects.get(id=id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('read', args=[data.slug]))   
        
    form = BookForm(instance=data)
    return render(request, "rental/edit_book.html", {
        'form': form
    })

def deleteBook(request, id):
    data = Book.objects.get(id=id)
    if request.method == "POST":
        data.delete()
        return HttpResponseRedirect('/home')
    
    return render(request, "rental/delete_book.html", {
        "data": data
    })

