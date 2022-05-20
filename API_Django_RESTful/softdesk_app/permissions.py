import pdb
from rest_framework.permissions import BasePermission


class HasProjectPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['retrieve', 'list', 'create']:
            return True
        elif view.action in ['update', 'partial_update', 'destroy']:
            return request.user.is_owner(view.kwargs['pk'])
        else :
            return request.user.is_contributor(view.kwargs['pk'])

    def has_object_permission(self, request, view, obj):
        if view.action=='retrieve':
            return True
        else:
            return obj.author_user==request.user


class HasIssueCommentPermission(BasePermission):
    def has_permission(self, request, view):
        if view.action in ['retrieve', 'list', 'create']:
            return request.user.is_contributor(view.kwargs['project_id'])
        elif view.action in ['update', 'partial_update', 'destroy']:
            return True

    def has_object_permission(self, request, view, obj):
        if view.action=='retrieve':
            return True
        else:
            return obj.author_user==request.user


class HasContributorPermission(BasePermission):
    def has_permission(self, request, view):
        return True