# Generated by Django 4.1.5 on 2023-01-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('text', models.TextField(max_length=150)),
                ('image', models.ImageField(upload_to='event_images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
