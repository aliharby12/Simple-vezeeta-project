# Generated by Django 2.2 on 2020-07-31 16:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200731_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='joined_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاريخ الانضمام'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='Specialist_doctor',
            field=models.CharField(choices=[('باطنة', 'باطنه'), ('جراحه تجميل', 'جراحه تجميل'), ('امراض دم', 'امراض دم'), ('مخ واعصاب', 'مخ واعصاب'), ('انف واذن', 'انف واذن'), ('اسنان', 'اسنان'), ('حميات', 'حميات'), ('اطفال', 'اطفال'), ('نسا وتوليد', 'نسا وتوليد'), ('جراحه عامه', 'جراحه عامه'), ('جراحه اطفال', 'جراحه اططفال'), ('اورام', 'اورام'), ('تخسيس', 'تخسيس'), ('عظام', 'عظام')], default='باطنه', max_length=255, verbose_name='التخصص'),
        ),
    ]