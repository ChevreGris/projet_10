# Generated by Django 4.0.4 on 2022-05-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('softdesk_app', '0006_alter_issue_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='permission',
            field=models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], max_length=255),
        ),
    ]
