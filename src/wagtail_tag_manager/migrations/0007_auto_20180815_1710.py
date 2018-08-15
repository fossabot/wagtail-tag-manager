# Generated by Django 2.0.6 on 2018-08-15 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_tag_manager', '0006_auto_20180330_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variable',
            name='variable_type',
            field=models.CharField(choices=[('HTTP', (('path', 'Path'), ('_repath+', 'Path with regex'))), ('User', (('user.pk', 'User'), ('session.session_key', 'Session'))), ('Wagtail', (('site', 'Site'),)), ('Other', (('_cookie+', 'Cookie'), ('_random', 'Random number')))], max_length=255),
        ),
    ]
