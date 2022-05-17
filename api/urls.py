from django.urls import path
from . import views


urlpatterns = [
    path("todos/", views.TodoList.as_view()),
    path("todo/<int:pk>", views.TodoRetrieveUpdateDestroy.as_view()),
    ]