from rest_framework import viewsets

from .models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = PublicationSerializer

    def get_queryset(self):
        return Publication.objects.all()
