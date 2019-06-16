from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny,]
        return super(ProjectViewSet, self).get_permissions()