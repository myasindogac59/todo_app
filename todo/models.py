from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# third party Apps
from autoslug import AutoSlugField 


class Category(models.Model):
  title = models.CharField(max_length=200)
  slug = AutoSlugField(populate_from='title', unique=True,)
  is_active = models.BooleanField(default=False)

  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return reverse(
      'category_view',
      kwargs= {
        "category_slug": self.slug
        }
      )

class Tag(models.Model):
  title = models.CharField(max_length=200)
  slug = AutoSlugField(populate_from='title', unique=True,)
  is_active = models.BooleanField(default=False)

  def get_absolute_url(self):
    return reverse(
      'tag_detail',
      kwargs= {
        "tag_slug": self.slug,
        
        }
      )

  def __str__(self):
    return self.title


class Todo(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  tag = models.ManyToManyField(Tag)
  # category = models.ForeignKey(Category, on_delete=models.CASCADE)
  #bu kullanılmayacak cunku CASCADE kullaninca tüm TODOlar silinir
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 
  title = models.CharField(max_length=200)
  content = models.TextField(blank=True, null=True)
  is_active = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def get_absolute_url(self):
    return reverse(
      'todo_detail',
      kwargs= {
        "category_slug": self.category.slug,
        'id':self.pk,
        }
      )

  def __str__(self):
    return self.title

