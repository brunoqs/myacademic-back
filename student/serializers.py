from rest_framework import serializers

from .models import Student
from project.models import Project
from study_group.models import StudyGroup

class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        field = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    study_groups = serializers.PrimaryKeyRelatedField(many=True, queryset=StudyGroup.objects.all())

    class Meta:
        model = Student
        fields = ('name', 'role', 'projects', 'study_groups')

    def create(self, validated_data):
        # pegando os dados do json
        projects_id = validated_data.pop('projects')
        study_groups_id = validated_data.pop('study_groups')

        student = Student()
        student.name = validated_data.pop('name')
        student.role = validated_data.pop('role')

        for project in projects_id:
            p = Project.objects.get(id=project)
            student.project.add(p)
        for study_group in study_groups_id:
            s = StudyGroup.objects.get(id=study_group)
            student.study_group.add(s)

        return student