from xml.etree.ElementInclude import include
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register("teams", views.TeamViewSet, basename="teams")

urlpatterns = [ 
    path("upload-teams/", views.TeamUploadAPIView.as_view(), name="upload-teams"),
    path("teams-list/", views.TeamsListAPIView.as_view(), name="teams-list"),
    path("", include(router.urls)),
]