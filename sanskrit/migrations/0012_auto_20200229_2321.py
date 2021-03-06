# Generated by Django 2.2.6 on 2020-02-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanskrit', '0011_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanskritlessons',
            name='lesson_icon',
            field=models.ImageField(default='design.png', upload_to='pics/'),
        ),
        migrations.AddField(
            model_name='sanskritquestions',
            name='desc_image',
            field=models.ImageField(default='design.png', upload_to='pics/'),
        ),
        migrations.AddField(
            model_name='sanskritquestions',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
