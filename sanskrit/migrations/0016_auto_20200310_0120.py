# Generated by Django 2.2.6 on 2020-03-09 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanskrit', '0015_auto_20200309_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanskritlessons',
            name='lessons_description',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
