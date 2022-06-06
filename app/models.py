from django.db import models

# Create your models here.

class Books(models.Model):
    book_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publish_date = models.DateField(auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.book_name   