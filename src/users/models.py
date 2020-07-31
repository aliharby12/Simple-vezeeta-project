from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Profile(models.Model):
    """create a database table for profiles"""
    user = models.OneToOneField(User, verbose_name=_('اسم المستخدم'), on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_('الاسم'))
    description = models.CharField(max_length=255, verbose_name=_('الوصف'))
    price = models.IntegerField(verbose_name=_('سعر الكشف'))

    class Meta:
        verbose_name = ('الملف الشخصي للمستخدم')
        verbose_name_plural = ('الملفات الشخصيه للمستخدمين')

    def __str__(self):
        """return the name of the user"""
        return self.name
