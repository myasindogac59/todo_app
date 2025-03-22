from django.shortcuts import render, get_object_or_404
from django.http import  Http404
from todo.models import Todo
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


def todo_details(request, id):
    todo = get_object_or_404(Todo, pk=id)
    context = dict(
      todo = todo
    )
    return render(request, 'todo/todo_details.html', context)