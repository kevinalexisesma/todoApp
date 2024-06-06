# Generated by Django 5.0.6 on 2024-05-16 03:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='prioryty',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is staff': False}, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='task', to=settings.AUTH_USER_MODEL),
        ),
    ]
