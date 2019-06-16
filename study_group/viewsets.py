from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import StudyGroup
from .serializers import StudyGroupSerializer


class StudyGroupViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = StudyGroupSerializer

    def get_queryset(self):
        return StudyGroup.objects.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny,]
        return super(StudyGroupViewSet, self).get_permissions()