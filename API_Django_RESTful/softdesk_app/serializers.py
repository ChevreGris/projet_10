from rest_framework.serializers import ModelSerializer
from softdesk_app.models import User, Contributor, Project, Issue, Comment


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['id']

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'author_user']


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id']