# Generated by Django 2.2 on 2020-07-31 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='الاسم')),
                ('description', models.CharField(max_length=255, verbose_name='الوصف')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='اسم المستخدم')),
            ],
            options={
                'verbose_name': 'الملف الشخصي للمستخدم',
                'verbose_name_plural': 'الملفات الشخصيه للمستخدمين',
            },
        ),
    ]