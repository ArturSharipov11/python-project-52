from django.urls import path
from task_manager.tasks import views

urlpatterns = [
    path('', views.IndexTasks.as_view(), name='tasks'),
    path('<int:pk>/', views.ShowTask.as_view(), name='view_task'),
    path('create/', views.CreateTask.as_view(), name='create_task'),
    path('<int:pk>/update/', views.UpdateTask.as_view(),
         name='update_task'),
    path('<int:pk>/delete/', views.DeleteTask.as_view(),
         name='delete_task')
]
