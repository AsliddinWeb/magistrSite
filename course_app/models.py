from django.db import models
from django.shortcuts import reverse

class CourseCategory(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Sarlavha",
        help_text="Kurs toifasining qisqa sarlavhasi."
    )
    cap_title = models.CharField(
        max_length=255,
        verbose_name="Bosh sarlavha",
        help_text="Toifa uchun asosiy bosh sarlavha."
    )
    description = models.TextField(
        verbose_name="Tavsif",
        help_text="Kurs toifasining batafsil tavsifi."
    )
    link = models.CharField(
        verbose_name="Havola",
        help_text="Toifaga havola yoki qo'shimcha ma'lumot sahifasi."
    )
    image = models.ImageField(
        upload_to='course_categories/',
        verbose_name="Rasm",
        help_text="Kurs toifasi uchun rasm."
    )
    file_image = models.ImageField(
        upload_to='course_images/',
        verbose_name="Fayl uchun rasm",
        help_text="Fayl uchun rasm."
    )
    bg_color = models.CharField(
        max_length=255,
        verbose_name="Orqa fon rangi",
        help_text="Orqa fon rangi.",
        default="#"
    )

    class Meta:
        verbose_name = "1. Kategoriya"
        verbose_name_plural = "1. Kategoriyalar"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_details', kwargs={'category_id': self.id})

class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, verbose_name="Kategoriya")

    title = models.CharField(
        max_length=255,
        verbose_name="Sarlavha",
        help_text="Kursning qisqa nomi yoki sarlavhasi."
    )
    description = models.TextField(
        verbose_name="Tavsif",
        help_text="Kursning batafsil tavsifi."
    )
    image = models.ImageField(
        upload_to='courses/',
        null=True,
        blank=True,
        verbose_name="Rasm",
        help_text="Kurs uchun rasm (ixtiyoriy)."
    )
    link = models.TextField(
        verbose_name="Havola",
        help_text="Kurs haqida qo'shimcha ma'lumot sahifasi yoki havola."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan vaqti",
        help_text="Kursning yaratilgan sanasi va vaqti."
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Yangilangan vaqti",
        help_text="Kursning oxirgi yangilangan sanasi va vaqti."
    )

    class Meta:
        verbose_name = "2. Mashg'ulot"
        verbose_name_plural = "2. Mashg'ulotlar"

    def __str__(self):
        return self.title
