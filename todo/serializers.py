from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . models import Task, Project
from django.core.exceptions import ValidationError, ObjectDoesNotExist

class CurrentProjectDefault(object):
    requires_context = True

    def __call__(self, serializer_field):
        try:
            self.project = Project.objects.get(
                id=serializer_field.context["request"].parse_context(
                    "project_id"
                )
            )
        except ObjectDoesNotExist:
            raise ValidationError("Project Does Not Exist")


        return self.object

class TaskSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "name", "project", "description", "last_modified")
        read_only_fields = ("id", "last_modified")