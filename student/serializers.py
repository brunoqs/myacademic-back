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
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all().values('id'))
    study_group = serializers.PrimaryKeyRelatedField(many=True, queryset=StudyGroup.objects.all().values('id'))

    class Meta:
        model = Student
        fields = ('name', 'role', 'project', 'study_group')

    def create(self, validated_data):
        # pegando os dados do json
        projects_id = validated_data.pop('project')
        study_groups_id = validated_data.pop('study_group')

        student = Student()
        student.name = validated_data.pop('name')
        student.role = validated_data.pop('role')
        student.save()

        for project in projects_id:
            p = Project.objects.get(id=project['id'])
            student.project.add(p)
        for study_group in study_groups_id:
            s = StudyGroup.objects.get(id=study_group['id'])
            student.study_group.add(s)

        return student