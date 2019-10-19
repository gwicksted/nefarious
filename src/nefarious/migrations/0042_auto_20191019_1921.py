# Generated by Django 2.1.5 on 2019-10-19 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0041_watchtvseasonrequest_date_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchmovie',
            options={'ordering': ('name',), 'permissions': (('can_immediately_watch_movie', 'Can immediately start watching movies'),)},
        ),
        migrations.AlterModelOptions(
            name='watchtvshow',
            options={'ordering': ('name',), 'permissions': (('can_immediately_watch_tv', 'Can immediately start watching tv shows'),)},
        ),
        migrations.AlterField(
            model_name='nefarioussettings',
            name='jackett_host',
            field=models.CharField(default='jackett', max_length=500),
        ),
        migrations.AlterField(
            model_name='nefarioussettings',
            name='jackett_port',
            field=models.IntegerField(default=9117),
        ),
        migrations.AlterField(
            model_name='nefarioussettings',
            name='transmission_host',
            field=models.CharField(default='transmission', max_length=500),
        ),
        migrations.AlterField(
            model_name='nefarioussettings',
            name='transmission_pass',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='nefarioussettings',
            name='transmission_port',
            field=models.IntegerField(default=9091),
        ),
        migrations.AlterField(
            model_name='nefarioussettings',
            name='transmission_user',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
