# Generated by Django 2.2 on 2020-07-31 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(verbose_name='سعر الكشف'),
        ),
    ]