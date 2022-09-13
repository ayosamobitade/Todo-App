from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from .serializers import TodoSerializer, TodocompleteSerializer
from todo.models import Todo
from rest_framework import permissions



class  TodoList(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user = user).order_by('-created')

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class TodoRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permissions = [permissions.IsAuthenticated]

    def get_query(self):
        user = self.request.user
        # user can only delete own post
        return Todo.objects.filter(user = user)

class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_class = [permisions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

