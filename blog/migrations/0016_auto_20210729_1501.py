# Generated by Django 3.2.4 on 2021-07-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_add_to_carousel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='add_to_carousel',
            field=models.CharField(choices=[('add_to_carousel', 'Yes'), ('remove_from_carousel', 'No')], default='remove_from_carousel', help_text='<small style="color: red; opacity: 0.5; font-weight: 300; font-size: 13px;">Carousel limited to 5 posts.</small>', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10),
        ),
    ]
