# Generated by Django 3.2.4 on 2021-07-09 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210709_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_large',
            field=models.CharField(choices=[('featured_small_1', 'Small Feature 1'), ('not-featured', '--'), ('featured_large', 'Large Feature')], default='not-featured', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='featured_small_1',
            field=models.CharField(choices=[('featured_small_1', 'Small Feature 1'), ('not-featured', '--'), ('featured_large', 'Large Feature')], default='not-featured', max_length=20),
        ),
    ]
