# Generated by Django 3.2.4 on 2021-07-29 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='user/avatar.jpg', upload_to='users/avatars/'),
        ),
    ]