from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerialzer):
    created = serializers.ReadOnlyField()
    complete = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'created', 'completed', 'slug']

        
