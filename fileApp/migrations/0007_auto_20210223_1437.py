# Generated by Django 3.1.7 on 2021-02-23 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileApp', '0006_remove_item_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='brand_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='brand_name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='product_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='fileApp.product', verbose_name='item'),
        ),
    ]
