# Generated by Django 4.1.10 on 2023-08-31 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_userprofile_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friend_of', to=settings.AUTH_USER_MODEL),
        ),
    ]