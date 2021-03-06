# Generated by Django 3.1.7 on 2021-02-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileApp', '0003_auto_20210223_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='logo',
            field=models.ImageField(upload_to='images/', verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]
