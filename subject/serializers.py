from rest_framework import serializers

from .models import Subject, SubjectContent


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('pk', 'name', 'type', 'contents',)
        read_only_fields = ('contents',)


class SubjectContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectContent
        fields = ('pk', 'fk', 'title', 'content',)

    def get_subject_content_cleaned_data(self, data):
        subject = Subject.objects.get(pk=data.get('fk', ''))

        response = {
            'fk': subject,
            'title': self.data.get('title', ''),
            'content': self.data.get('content', ''),
        }

        return response

    def save(self, request, **kwargs):
        if self.instance is None:
            content = self.create(request)
            return content

    def create(self, request):
            content_fields = self.get_subject_content_cleaned_data(request.data)
            content = SubjectContent(**content_fields)
            content.save()

            return content
