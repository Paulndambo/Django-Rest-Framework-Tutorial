from django.urls import path
from . import views


urlpatterns = [ 
    path("tasks/", views.TaskBulkAPIView.as_view(), name="tasks"),
]