# Generated by Django 2.1.5 on 2019-08-12 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0038_auto_20190810_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchmovie',
            name='renamed',
        ),
        migrations.RemoveField(
            model_name='watchtvepisode',
            name='renamed',
        ),
        migrations.RemoveField(
            model_name='watchtvseason',
            name='renamed',
        ),
    ]
