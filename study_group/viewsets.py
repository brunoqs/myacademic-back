from rest_framework import viewsets

from .models import StudyGroup
from .serializers import StudyGroupSerializer


class StudyGroupViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = StudyGroupSerializer

    def get_queryset(self):
        return StudyGroup.objects.all()
