import pdb
from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Project, User, Issue, Comment, Contributor

owner_methods = ("PUT", "PATCH", "DELETE")
contrib_methods = ("POST", "GET")


class HasContributorPermission(BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(id=view.kwargs['project_id'])
        if project in Project.objects.filter(contributors__user=request.user):
            project = Project.objects.get(id=view.kwargs['project_id'])
            if request.method in SAFE_METHODS:
                return True
            return request.user == project.author_user
        return False


class HasProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'create']:
            return True
        elif view.action in ["update", "partial_update", "destroy"]:
            return request.user.is_owner(view.kwargs['pk'])
        else :
            return request.user.is_contributor(view.kwargs['pk'])


class HasIssuePermission(BasePermission):
    def has_permission(self, request, view):
        return True
        if Contributor.objects.filter(user=request.user).filter(project=view.kwargs['project_id']).exists():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        return True
        if request.method in owner_methods:
            if obj.author_user == request.user:
                return True
        else:
            return request.user == obj.author_user


class HasCommentPermission(BasePermission):
    def has_permission(self, request, view):
        return True
        if Contributor.objects.filter(user=request.user).filter(project=view.kwargs['project_id']).exists():
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in owner_methods:
            return True
            if obj.author_user_id == request.user:
                return True
        else:
            return request.user == obj.author_user_id