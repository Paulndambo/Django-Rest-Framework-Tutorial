from rest_framework import serializers
from .models import Team
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)

class TeamUploadSerializer(serializers.Serializer):
    file = serializers.FileField()


class TeamSaveSerializer(serializers.Serializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"



class TeamBulkSerializer(BulkSerializerMixin, serializers.ModelSerializer):
    class Meta(object):
        model = Team
        # only necessary in DRF3
        fields = "__all__"
        list_serializer_class = BulkListSerializer