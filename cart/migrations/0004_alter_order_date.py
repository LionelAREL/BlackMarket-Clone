# Generated by Django 4.0.4 on 2022-05-05 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
