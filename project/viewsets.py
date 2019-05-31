from rest_framework import viewsets

from .serializers import ProjectSerializer
from .models import Project

class ProjectViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        return Project.objects.all()