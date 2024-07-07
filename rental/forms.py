from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta():
        model = Book
        exclude = ['slug']

        labels = {
            "book_name": "Enter the name of the Book:",
            "author_name": "Enter the name of the Author:",
            "cover_image": "Upload an image of the book cover:",
            "summary": "Enter the book summary:",
            "author_email": "Enter the author's email id:",
            "rating": "Enter the rating for the book:",
            "cost": "Enter the cost of the book in dollars",
            "status": "Is this book available to rent?" ### HAVE TO CHANGE LATER
        }