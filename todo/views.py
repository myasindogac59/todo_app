from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
# my models:
from todo.models import Todo, Category, Tag

@login_required(login_url='/admin/login')
def home_view(request):
  todos = Todo.objects.filter(
    user = request.user,
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
@login_required(login_url='/admin/login')
def category_view(request, category_slug):
  category = get_object_or_404(Category, slug=category_slug)
  todos = Todo.objects.filter(
    is_active=True,
    category=category,
    user=request.user
  )
  context = dict(
    category= category,
    todos = todos,
  )
  return render(request, 'todo/todo_list.html', context)


@login_required(login_url='/admin/login')
def todo_details(request, category_slug, id):
    todo = get_object_or_404(
      Todo,
      category__slug=category_slug,
      pk=id,
      user=request.user,
      )
    context = dict(
      todo = todo
    )
    return render(request, 'todo/todo_details.html', context)

@login_required(login_url='/admin/login')
def tag_detail(request, tag_slug):
  tag = get_object_or_404(Tag, slug=tag_slug)
  context = dict(
    tag =tag,
    todos = tag.todo_set.filter(user=request.user)
  )
  return render(request, 'todo/todo_list.html', context)