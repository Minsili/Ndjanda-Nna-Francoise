# Generated by Django 5.0.4 on 2024-06-18 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='NnaCategory',
        ),
        migrations.RenameModel(
            old_name='FAQ',
            new_name='NnaFAQ',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='NnaUser',
        ),
    ]
