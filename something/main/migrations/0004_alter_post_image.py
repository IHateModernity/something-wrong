# Generated by Django 5.0.1 on 2024-01-10 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='Noimage.png', max_length=56, upload_to='', verbose_name='Image'),
        ),
    ]
