from urllib import request
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from softdesk_app.models import User, Contributor, Project, Issue, Comment
from softdesk_app.serializers import UserSerializer, ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import (HasProjectPermission, HasContributorPermission, HasIssueCommentPermission)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasProjectPermission]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(Q(author_user=self.request.user) | Q(contributor__user=self.request.user))

class IssueViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasIssueCommentPermission]
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs['project_id'])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['project_id'] = self.kwargs['project_id']
        return context

class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasIssueCommentPermission]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(issue__project_id=self.kwargs['project_id'], issue_id=self.kwargs['issue_id'])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['issue_id'] = self.kwargs['issue_id']
        return context


class ContributorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasContributorPermission]
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
