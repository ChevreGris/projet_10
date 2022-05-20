from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def is_owner(self, project_id):
        return Project.objects.filter(pk=project_id, author_user=self).exists()

    def is_contributor(self, project_id):
        return self.is_owner(project_id) or Contributor.objects.filter(user=self, project=project_id).exists()


class Project(models.Model):
    TYPES = [('BE', 'back-end'),
             ('FE', 'front-end'),
             ('IOS', 'ios'),
             ('AD', 'android')
    ]
    
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TYPES)
    author_user = models.ForeignKey('User', on_delete=models.CASCADE)


class Issue(models.Model):
    TAGS = [('BUG', 'bug'),
            ('UPGRADE', 'upgrade'),
            ('TASK', 'task')
    ]

    PRIORITY = [('LOW', 'low'),
                ('MED', 'medium'),
                ('HIGH', 'high')
    ]

    STATUS = [('TO_DO', 'to_do'),
              ('IN_PROGRESS', 'in_progress'),
              ('DONE', 'done')
    ]
    
    title = models.CharField(max_length=255)
    desk = models.CharField(max_length=255)
    tag = models.CharField(max_length=255, choices=TAGS)
    priority = models.CharField(max_length=255, choices=PRIORITY)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=STATUS)
    author_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='created_issues')
    assignee_user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='assigned_issues', null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    description = models.CharField(max_length=255)
    author_user = models.ForeignKey('User', on_delete=models.CASCADE)
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Contributor(models.Model):
    CHOIX = [('oui', 'oui'),
              ('non', 'non')
    ]

    user = models.ForeignKey('User', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    permission = models.CharField(max_length=255, choices=CHOIX)
    role = models.CharField(max_length=255)
