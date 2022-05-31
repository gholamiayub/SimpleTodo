from django.urls import path

from todos.views import create_todo, list_todos, update_todo, delete_todo

urlpatterns = [
    path('create/', create_todo, name="create"),
    path('list/', list_todos, name="list"),
    path('update/<int:todo_id>/', update_todo, name="update"),
    path('delete/<int:todo_id>/', delete_todo, name="delete")
]