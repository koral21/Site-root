# Generated by Django 4.1.5 on 2023-01-09 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_rename_post_eventconfig'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventConfig',
            new_name='Post',
        ),
    ]
