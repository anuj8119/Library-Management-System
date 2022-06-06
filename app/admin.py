from django.contrib import admin
from .models import *
# Register your models here.



class BookAdmin(admin.ModelAdmin):
    list_display = (
        'book_name','author_name', 'price', 'publish_date', 'created')

admin.site.register(Books, BookAdmin)