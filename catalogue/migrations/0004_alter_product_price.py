# Generated by Django 4.0.4 on 2022-05-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_alter_product_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]