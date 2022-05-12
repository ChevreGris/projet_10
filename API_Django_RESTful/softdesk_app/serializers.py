from rest_framework.serializers import ModelSerializer
from softdesk_app.models import User, Contributor, Project, Issue, Comment


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id', 'user', 'project', 'permission', 'role']
        read_only_fields = ['id']


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'type', 'id', 'author_user']
        read_only_fields = ['id', 'author_user']

    def create(self, validated_data):
        validated_data['author_user'] = self.context['request'].user
        return Project.objects.create(**validated_data)


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'desk', 'tag', 'priority', 'project', 'status',
                  'author_user', 'assignee_user', 'created_time']
        read_only_fields = ['id', 'project', 'author_user', 'assignee_user', 'created_time']

    def create(self, validated_data):
        validated_data['project'] = Project.objects.get(pk=self.context['project_id'])
        validated_data['author_user'] = self.context['request'].user
        return Issue.objects.create(**validated_data)


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'description', 'author_user', 'issue', 'created_time']
        read_only_fields = ['id']
