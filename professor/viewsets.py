from rest_framework import viewsets

from .models import Professor
from .serializers import ProfessorSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = ProfessorSerializer

    def get_queryset(self):
        return Professor.objects.all()
