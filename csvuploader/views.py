
from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from .models import Team
import io, csv, pandas as pd
from .serializers import TeamSaveSerializer, TeamUploadSerializer, TeamSerializer, TeamBulkSerializer
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import action
fs = FileSystemStorage(location='temp')
from rest_framework_bulk import (
    BulkListSerializer,
    BulkSerializerMixin,
    ListBulkCreateUpdateDestroyAPIView,
)
# Create your views here.
class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer



class TaskBulkAPIView(ListBulkCreateUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamBulkSerializer


class TeamUploadAPIView(generics.CreateAPIView):
    serializer_class = TeamUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "temp.csv", file_content
        )
        temp_file = fs.path(file_name)
        csv_file = open(temp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)
        team_list = []
        for id_, row in enumerate(reader):
            (
                name, 
                country,
                stadium
            ) = row
            team_list.append(Team(name=name, country=country, stadium=stadium))
        Team.objects.bulk_create(team_list)
        """
        reader = pd.read_csv(file)
        for row in reader.iterrows():
            new_team = Team(
                name = row['name'],
                country = row['country'],
                stadium = row['stadium']
            )
            new_team.save()
            """
        return Response({"success": "File Uploaded Successfully"}, status=status.HTTP_201_CREATED)


class TeamsListAPIView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSaveSerializer

    def get(self, request):
        teams = Team.objects.all()
        serializer = self.serializer_class(instance=teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)