# Generated by Django 2.0.2 on 2019-07-27 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190727_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='images',
            new_name='image',
        ),
    ]
