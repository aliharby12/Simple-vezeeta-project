from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify

TYPE_OF_PERSON=(
    ('M', "Male"),
    ('F', "Female"),
)

class Profile(models.Model):
    """create a database table for profiles"""

    DOCTOR_IN={
        ('باطنة', 'باطنه'),
        ('حميات', 'حميات'),
        ('اسنان', 'اسنان'),
        ('اطفال', 'اطفال'),
        ('مخ واعصاب', 'مخ واعصاب'),
        ('عظام', 'عظام'),
        ('نسا وتوليد', 'نسا وتوليد'),
        ('انف واذن', 'انف واذن'),
        ('جراحه عامه', 'جراحه عامه'),
        ('جراحه تجميل', 'جراحه تجميل'),
        ('جراحه اطفال', 'جراحه اططفال'),
        ('تخسيس', 'تخسيس'),
        ('اورام', 'اورام'),
        ('امراض دم', 'امراض دم'),
    }

    user = models.OneToOneField(User, verbose_name=_('اسم المستخدم'), on_delete=models.CASCADE)
    name = models.CharField(_('الاسم'), max_length=255, null=True, blank=True)
    description = models.CharField(_('الوصف'), max_length=255, null=True, blank=True)
    address = models.CharField(_('المحافظه'), max_length=255, null=True, blank=True)
    address_detail = models.CharField(_('العنوان بالتفصيل'), max_length=255, null=True, blank=True)
    phone = models.CharField(_(' رقم الهاتف'), max_length=255, null=True, blank=True)
    working_hours = models.IntegerField(_('ساعات العمل'), default=1)
    Waiting_time = models.IntegerField(_('مدة الانتظار'), default=1)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    google = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, choices=TYPE_OF_PERSON, null=True, blank=True)
    price = models.IntegerField(_('سعر الكشف'), null=True, blank=True)
    image = models.ImageField(_('الصوره الشخصية'), upload_to='profile', null=True, blank=True)
    slug = models.SlugField(_('slug'), blank=True, null=True)
    Specialist_doctor = models.CharField(_('التخصص'), choices=DOCTOR_IN, max_length=255, default='باطنه')
    joined_at = models.DateTimeField(_('تاريخ الانضمام'), auto_now_add=True)

    def save(self, *args, **kwargs):
        """paypass the save function to save the username as slug"""
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

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
