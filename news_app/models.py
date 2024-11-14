from django.db import models

class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Kategoriya nomi",
        help_text="Kategoriyaning nomini kiriting"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan sana",
        help_text="Kategoriya yaratilgan vaqt"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Yangilangan sana",
        help_text="Kategoriya yangilangan vaqt"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class News(models.Model):
    image = models.ImageField(
        upload_to='news-images',
        verbose_name="Yangilik rasmi",
        help_text="Yangilik rasmini kiriting"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Yangilik sarlavhasi",
        help_text="Yangilikning sarlavhasini kiriting"
    )
    content = models.TextField(
        verbose_name="Yangilik matni",
        help_text="Yangilikning to'liq matnini kiriting"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="news",
        verbose_name="Kategoriya",
        help_text="Yangilik tegishli bo'lgan kategoriyani tanlang"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Yaratilgan sana",
        help_text="Kategoriya yaratilgan vaqt"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Yangilangan sana",
        help_text="Kategoriya yangilangan vaqt"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-created_at']
