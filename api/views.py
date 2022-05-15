from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .serializers import TodoSerializer
from todo.models import Todo


class  TodoList(ListAPIView):
    serializer_class = TodoSerializer


    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user = user).order_by('-created')

        