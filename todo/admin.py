from django.contrib import admin
from .models import (Todo, Category)
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
  list_display = [
    'pk',
    'title',
    'is_active',
  ]

  

class TodoAdmin(admin.ModelAdmin):
  list_display = [
    'pk',
    'category',
    'title',
    'is_active',
    'created_at',
    'updated_at',
  ]

  list_display_links = [ # admin panelde tıklanabilir olması için <--
    'pk',
    'category',
    'title',
  ]

admin.site.register(Todo, TodoAdmin)
admin.site.register(Category, CategoryAdmin)