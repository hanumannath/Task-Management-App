from django.urls import path
from .views import TaskCreateView, AssignTaskAPIView, GetTasksByUserAPIView

urlpatterns = [
    path('create/', TaskCreateView.as_view()),
    path('assign/<int:task_id>/', AssignTaskAPIView.as_view()),
    path('user_tasks/<int:user_id>/', GetTasksByUserAPIView.as_view()),
]
