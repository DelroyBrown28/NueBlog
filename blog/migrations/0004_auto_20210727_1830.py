# Generated by Django 3.2.4 on 2021-07-27 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210727_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-published',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='publish',
            new_name='published',
        ),
    ]