# Generated by Django 4.1.7 on 2023-03-18 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_people'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='desc',
            new_name='desc1',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='img',
            new_name='img1',
        ),
        migrations.RenameField(
            model_name='people',
            old_name='name',
            new_name='name1',
        ),
    ]
