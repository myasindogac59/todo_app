"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from config.views import logout_view
from todo.views import (home_view, todo_details, category_view, tag_detail)
urlpatterns = [
    path('', home_view),
    path('category/<slug:category_slug>/', category_view, name='category_view' ),
    path('tag/<slug:tag_slug>/', tag_detail, name='tag_detail' ),
    path('category/<slug:category_slug>/todo/<int:id>/', todo_details, name='todo_detail' ),
    path('logout/', logout_view, name='logout_view'),
    # path('todo/<int:id>/', todo_details, name='todo_detail' ),
    path('admin/', admin.site.urls),
]
