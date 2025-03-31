from django.shortcuts import render, get_object_or_404
from django.http import  Http404
from todo.models import Todo, Category
# Create your views here.
def home_view(request):
  todos = Todo.objects.filter(
    is_active = True,
    # title__icontains = 'todo'
  )
  context = dict(
    todos = todos,
  )
  return render(request, 'todo/todo_list.html', context)

# def todo_details(request, id):
#   try:
#     todo = Todo.objects.get(pk=id)
#     context = dict(
#       todo = todo
#     )
#     return render(request, 'todo/todo_details.html', context)
#   except Todo.DoesNotExist:
#       raise Http404

def category_view(request, category_slug):
  category = get_object_or_404(Category, slug=category_slug)
  todos = Todo.objects.filter(
    is_active=True,
    category=category,
  )
  context = dict(
    todos = todos,
    category= category,
  )
  return render(request, 'todo/todo_list.html', context)



def todo_details(request, category_slug, id):
    todo = get_object_or_404(Todo, category__slug=category_slug , pk=id)
    context = dict(
      todo = todo
    )
    return render(request, 'todo/todo_details.html', context)