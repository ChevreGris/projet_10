# Generated by Django 4.0.4 on 2022-05-03 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignee_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_issues', to=settings.AUTH_USER_MODEL),
        ),
    ]
