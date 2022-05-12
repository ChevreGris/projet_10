from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from softdesk_app.models import User, Contributor, Project, Issue, Comment
from softdesk_app.serializers import UserSerializer, ContributorSerializer, ProjectSerializer, IssueSerializer, CommentSerializer
from .permissions import (HasProjectPermission, HasContributorPermission, HasIssuePermission, HasCommentPermission)


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasProjectPermission]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class IssueViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasIssuePermission]
    serializer_class = IssueSerializer

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs['project_id'])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['project_id'] = self.kwargs['project_id']
        return context

class CommentViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasCommentPermission]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ContributorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, HasContributorPermission]
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
