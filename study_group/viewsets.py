from rest_framework import viewsets

from .serializers import StudyGroupSerializer
from .models import StudyGroup

class StudyGroupViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = StudyGroupSerializer
    
    def get_queryset(self):
        return StudyGroup.objects.all()