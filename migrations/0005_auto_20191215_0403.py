# Generated by Django 2.2.5 on 2019-12-14 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_auto_20191215_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(verbose_name='Hello'),
        ),
    ]
