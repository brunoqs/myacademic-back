from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Professor
from .serializers import ProfessorSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        return Professor.objects.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny,]
        return super(ProfessorViewSet, self).get_permissions()