from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=60)
    cover_image = models.ImageField(upload_to="images")
    summary = models.TextField()
    author_email = models.EmailField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):    
        self.slug = slugify(self.book_name)
        super(Book, self).save(*args, **kwargs) 