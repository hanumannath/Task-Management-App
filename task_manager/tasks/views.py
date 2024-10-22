from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskCreateSerializer, TaskSerializer


class TaskCreateView(APIView):
    """
    API View for creating a new task.

    This view handles POST requests to create a task with a name and description.
    It validates the input data using the TaskCreateSerializer and returns the
    created task's data upon successful creation.
    """

    def post(self, request):
        """
        Handle POST request to create a task.

        Args:
            request: The request object containing the task data.

        Returns:
            Response: A response containing the created task data or errors.
        """
        serializer = TaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssignTaskAPIView(APIView):
    """
    API View for assigning a task to one or multiple users.

    This view handles PATCH requests to assign a task to specified user IDs.
    It validates the user IDs provided in the request and returns a response
    indicating the success of the operation and any invalid user IDs.
    """

    def patch(self, request, task_id):
        """
        Handle PATCH request to assign users to a task.

        Args:
            request: The request object containing user IDs.
            task_id: The ID of the task to which users will be assigned.

        Returns:
            Response: A response indicating the result of the assignment operation.
        """
        task = get_object_or_404(Task, id=task_id)
        user_ids = request.data.get('user_ids', [])

        if not user_ids:
            return Response({'error': 'At least one user ID must be provided.'}, status=status.HTTP_400_BAD_REQUEST)

        valid_users = User.objects.filter(id__in=user_ids)
        valid_user_ids = valid_users.values_list('id', flat=True)
        invalid_user_ids = list(set(user_ids) - set(valid_user_ids))

        task.assigned_users.add(*valid_users)
        task.save()

        response_data = {
            'message': f'{len(list(valid_user_ids))} Users assigned successfully',
            'task_id': task.id,
            'invalid_user_ids': invalid_user_ids
        }

        return Response(response_data, status=status.HTTP_200_OK)


class GetTasksByUserAPIView(generics.ListAPIView):
    """
    API View for retrieving tasks assigned to a specific user.

    This view handles GET requests to fetch all tasks assigned to a user based
    on the user ID provided in the URL.
    """

    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Get tasks assigned to the specified user.

        Args:
            None

        Returns:
            QuerySet: A queryset of tasks assigned to the user.
        """
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        return Task.objects.filter(assigned_users=user)
