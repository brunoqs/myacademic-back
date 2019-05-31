from rest_framework import viewsets

from .serializers import StudentSerializer
from .models import Student

class StudentViewSet(viewsets.ModelViewSet):
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAdminUser, )
    serializer_class = StudentSerializer
    
    def get_queryset(self):
        return Student.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = StudentSerializer(instance=instance)
    #     return Response(serializer.data)
        