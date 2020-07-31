from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save


class Profile(models.Model):
    """create a database table for profiles"""
    user = models.OneToOneField(User, verbose_name=_('اسم المستخدم'), on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name=_('الاسم'))
    description = models.CharField(max_length=255, verbose_name=_('الوصف'))
    price = models.IntegerField(verbose_name=_('سعر الكشف'), null=True, blank=True)
    image = models.ImageField(_('الصوره الشخصية'), upload_to='profile')

    class Meta:
        verbose_name = ('الملف الشخصي للمستخدم')
        verbose_name_plural = ('الملفات الشخصيه للمستخدمين')

    def __str__(self):
        """return the name of the user"""
        return '%s' %(self.user.username)

def create_profile(sender, **kwargs):
    """create a function to create a profile just create a  user"""
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
