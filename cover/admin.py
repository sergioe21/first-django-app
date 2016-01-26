from django.contrib import admin

# Register your models here.

from .models import Person, Page

admin.site.register(Person)
admin.site.register(Page)