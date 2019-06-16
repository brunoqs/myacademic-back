from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = PublicationSerializer

    def get_queryset(self):
        return Publication.objects.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny,]
        return super(PublicationViewSet, self).get_permissions()