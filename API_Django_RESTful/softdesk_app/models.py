from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Contributor(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    permission = models.BooleanField()
    role = models.CharField(max_length=255)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    author_user = models.ForeignKey('User', on_delete=models.CASCADE)


class Issue(models.Model):
    title = models.CharField(max_length=255)
    desk = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    author_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='created_issues')
    assignee_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='assigned_issues')
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=255)
    author_user = models.ForeignKey('User', on_delete=models.CASCADE)
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)