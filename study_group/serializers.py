from rest_framework import serializers

from study_group.models import StudyGroup


class StudyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyGroup
        fields = '__all__'
