# Generated by Django 3.2.4 on 2021-07-10 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='large_feature',
            field=models.BooleanField(),
        ),
    ]
