from rest_framework import serializers
from .models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description']

    def create(self, validated_data):
        return Task.objects.create(
            name=validated_data['name'],
            description=validated_data.get('description', ''),
            status='pending'
        )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'task_type', 'completed_at', 'status']
