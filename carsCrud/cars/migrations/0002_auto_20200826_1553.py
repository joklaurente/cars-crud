# Generated by Django 3.1 on 2020-08-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
