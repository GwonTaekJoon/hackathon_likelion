# Generated by Django 2.1.8 on 2019-08-09 15:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locally', '0002_apply_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joboffer',
            name='user',
        ),
        migrations.AddField(
            model_name='joboffer',
            name='joboffer_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
