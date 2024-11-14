from django.db import models

class HomeWelcome(models.Model):
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Rasm',
        help_text='Foydalanuvchiga ko‘rsatiladigan rasmni yuklang'
    )
    stat_title = models.CharField(
        max_length=255,
        verbose_name='Statistik Sarlavha',
        help_text='Qisqacha statistik sarlavha kiriting'
    )
    stat_text = models.TextField(
        verbose_name='Statistik Matn',
        help_text='Statistika haqida batafsil matn kiriting'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Sarlavha',
        help_text='Asosiy sahifa uchun sarlavha kiriting'
    )
    body = models.TextField(
        verbose_name='Matn',
        help_text='Asosiy sahifa uchun to‘liq matn kiriting'
    )

    class Meta:
        verbose_name = '1. Hush kelibsiz'
        verbose_name_plural = '1. Hush kelibsiz'

    def __str__(self):
        return self.title

class HomeWelcomeButton(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Tugma Sarlavhasi',
        help_text='Tugmada ko‘rsatiladigan sarlavhani kiriting'
    )
    link = models.CharField(
        verbose_name='Havola',
        help_text='Tugma bosilganda yo‘naltiriladigan URL havolani kiriting'
    )
    css_class = models.TextField(
        verbose_name='CSS Class',
        help_text='Tugmaga qo‘llanadigan CSS class nomini kiriting'
    )

    class Meta:
        verbose_name = '1. Hush kelibsiz tugmalar'
        verbose_name_plural = '1. Hush kelibsiz tugmalar'

    def __str__(self):
        return self.title


class CourseRightButton(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Tugma Sarlavhasi',
        help_text='Tugmada ko‘rsatiladigan sarlavhani kiriting'
    )
    link = models.CharField(
        verbose_name='Havola',
        help_text='Tugma bosilganda yo‘naltiriladigan URL havolani kiriting'
    )
    css_class = models.TextField(
        verbose_name='CSS Class',
        help_text='Tugmaga qo‘llanadigan CSS class nomini kiriting'
    )

    class Meta:
        verbose_name = "3. Fan mashg'ulotlari o'ng tugmasi"
        verbose_name_plural = "3. Fan mashg'ulotlari o'ng tugmalari"

    def __str__(self):
        return self.title
