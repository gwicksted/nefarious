# Generated by Django 2.1.5 on 2019-10-24 17:59

from django.db import migrations
import jsonfield.encoder
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0047_nefarioussettings_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='nefarioussettings',
            name='tmdb_languages',
            field=jsonfield.fields.JSONField(blank=True, dump_kwargs={'cls': jsonfield.encoder.JSONEncoder, 'separators': (',', ':')}, load_kwargs={}, null=True),
        ),
    ]
