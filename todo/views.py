from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from . serializers import TaskSerializer
from rest_framework.serializers import ModelSerializer
from . models import Task
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
# Create your views here.
class TaskCreateAPIView(CreateAPIView):
    serializer_class = TaskSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs['many'] = True 

        return super("TaskCreateAPIView", self).get_serializer(*args, **kwargs)

class TaskBulkSerializer(BulkSerializerMixin, ModelSerializer):
    class Meta(object):
        model = Task
        # only necessary in DRF3
        fields = "__all__"
        list_serializer_class = BulkListSerializer

class TaskBulkAPIView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskBulkSerializer