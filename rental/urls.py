from django.urls import path
from . import views

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('add', views.CreateBookView.as_view(), name='create'),
    path('home/<slug:slug>', views.DetailedBookView.as_view(), name='read'),
    path('edit/<int:id>', views.editBook, name='update'),
    path('delete/<int:id>', views.deleteBook, name='delete')

]
