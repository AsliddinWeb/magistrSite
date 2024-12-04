# Generated by Django 5.1.3 on 2024-11-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0009_aboutresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_author/', verbose_name='Rasm')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('address', models.CharField(max_length=255, verbose_name='Manzil')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefon raqami')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': '8. Muallif haqida',
                'verbose_name_plural': '8. Muallif haqida',
            },
        ),
    ]