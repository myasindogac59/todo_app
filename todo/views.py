from django.shortcuts import render
from django.http import HttpResponse
from todo.models import Todo
# Create your views here.
def home_view(request):
  todos = Todo.objects.filter(is_active = True)
  context = dict(
    todos = todos
  )
  return render(request, 'todo/todo_list.html', context)