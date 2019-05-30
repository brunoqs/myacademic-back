from rest_framework import serializers

from .models import Student
from project.models import Project
from study_group.models import StudyGroup

class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = ('id', )

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', )

class StudentSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(many=True)
    study_group = StudyGroupSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        # pegando os dados do json
        projects_id = validated_data.pop('project')
        study_groups_id = validated_data.pop('study_group')
        print(projects_id)

        student = Student()
        student.name = validated_data.pop('name')
        student.role = validated_data.pop('role')

        for idx in projects_id:
            print(idx)
            p = Project.objects.get(id=idx)
            student.project.add(p)
            
        for idx in study_groups_id:
            s = StudyGroup.objects.get(id=idx)
            student.study_group.add(s)

        return student