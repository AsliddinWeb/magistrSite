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
        verbose_name = '2. Hush kelibsiz tugmalar'
        verbose_name_plural = '2. Hush kelibsiz tugmalar'

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
        verbose_name_plural = "3. Fan mashg'ulotlari o'ng tugmasi"

    def __str__(self):
        return self.title

class Message(models.Model):
    name = models.CharField(max_length=455, verbose_name='Ism familiya')
    phone = models.CharField(max_length=455, verbose_name='Telefon raqam')
    message = models.TextField(verbose_name='Xabar')
    is_read = models.BooleanField(default=False, verbose_name="O'qilganmi?")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "4. Xabar"
        verbose_name_plural = "4. Xabarlar"

class AboutWelcome(models.Model):
    title = models.CharField(max_length=455, verbose_name='Sarlavha')
    body = models.TextField(verbose_name='Matn')
    image = models.ImageField(upload_to='about', verbose_name='Rasm')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "5. Muallif haqida"
        verbose_name_plural = "5. Muallif haqida"

class AboutTeam(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    cap_title = models.CharField(max_length=255, verbose_name="Qisqa sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    image = models.ImageField(upload_to='about_team/', verbose_name="Rasm", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "6. Jamoadagi kishilar"
        verbose_name_plural = "6. Jamoadagi kishilar"

class AboutResult(models.Model):
    svg = models.TextField(verbose_name="SVG")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "7. Natijalar"
        verbose_name_plural = "7. Natijalar"

class AboutAuthor(models.Model):
    image = models.ImageField(upload_to='about_author/', verbose_name="Rasm")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    address = models.CharField(max_length=255, verbose_name="Manzil")
    phone = models.CharField(max_length=20, verbose_name="Telefon raqami")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "8. Muallif haqida"
        verbose_name_plural = "8. Muallif haqida"

class Quiz(models.Model):
    question = models.CharField(max_length=255, verbose_name="Savol")

    option_a = models.CharField(max_length=255, verbose_name="Javob A")
    option_b = models.CharField(max_length=255, verbose_name="Javob B")
    option_c = models.CharField(max_length=255, verbose_name="Javob C")
    option_d = models.CharField(max_length=255, verbose_name="Javob D")
    correct_option = models.CharField(
        max_length=1,
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')],
        verbose_name="To‘g‘ri javob"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "9. Savol"
        verbose_name_plural = "9. Savollar"