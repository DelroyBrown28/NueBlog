# Generated by Django 3.2.4 on 2021-07-14 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='small_feature_1',
            new_name='small_feature',
        ),
        migrations.RemoveField(
            model_name='post',
            name='small_feature_2',
        ),
    ]