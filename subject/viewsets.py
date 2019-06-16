from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.permissions import AllowAny

from .models import Subject
from .serializers import SubjectSerializer, SubjectContentSerializer


class SubjectViewSet(ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = SubjectSerializer

    def get_queryset(self):
        return Subject.objects.all()

    # endpoint para cadastro de um conteúdo de uma disciplina
    @action(methods=['post'], detail=True, url_path='content',
            url_name='content')
    def approve(self, request, pk=None):
        json = {"Details": "Disciplina não encontrada"}

        # só verifica se existe o Subject
        try:
            subject = Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Response(json, status=HTTP_400_BAD_REQUEST)

        serializer = SubjectContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(request)
            return Response(serializer.data, status=HTTP_201_CREATED)

        return Response(json, status=HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.permission_classes = [AllowAny,]
        return super(SubjectViewSet, self).get_permissions()
