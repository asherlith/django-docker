from django.contrib import admin

from .models import Book

# for adding the model to django admin  and getting access to models
admin.site.register(Book)
