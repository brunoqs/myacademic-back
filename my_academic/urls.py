"""my_academic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from professor.viewsets import ProfessorViewSet
from project.viewsets import ProjectViewSet
from publication.viewsets import PublicationViewSet
from student.viewsets import StudentViewSet
from study_group.viewsets import StudyGroupViewSet
from subject.viewsets import SubjectViewSet

router = routers.DefaultRouter()
router.register('professor', ProfessorViewSet, basename='professor')
router.register('projeto', ProjectViewSet, basename='projeto')
router.register('publicacao', PublicationViewSet, basename='publicacao')
router.register('estudante', StudentViewSet, basename='estudante')
router.register('grupo-estudo', StudyGroupViewSet, basename='grupo-estudo')
router.register('disciplina', SubjectViewSet, basename='disciplina')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
