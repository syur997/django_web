# Generated by Django 3.2.16 on 2022-11-15 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_rename_subject_fileupload_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='content',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='create_date',
        ),
    ]