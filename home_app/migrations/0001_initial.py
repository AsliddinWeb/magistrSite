# Generated by Django 5.1.3 on 2024-11-12 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWelcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Foydalanuvchiga ko‘rsatiladigan rasmni yuklang', upload_to='images/', verbose_name='Rasm')),
                ('stat_title', models.CharField(help_text='Qisqacha statistik sarlavha kiriting', max_length=255, verbose_name='Statistik Sarlavha')),
                ('stat_text', models.TextField(help_text='Statistika haqida batafsil matn kiriting', verbose_name='Statistik Matn')),
                ('title', models.CharField(help_text='Asosiy sahifa uchun sarlavha kiriting', max_length=255, verbose_name='Sarlavha')),
                ('body', models.TextField(help_text='Asosiy sahifa uchun to‘liq matn kiriting', verbose_name='Matn')),
            ],
            options={
                'verbose_name': '1. Hush kelibsiz',
                'verbose_name_plural': '1. Hush kelibsiz',
            },
        ),
        migrations.CreateModel(
            name='HomeWelcomeButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Tugmada ko‘rsatiladigan sarlavhani kiriting', max_length=255, verbose_name='Tugma Sarlavhasi')),
                ('link', models.CharField(help_text='Tugma bosilganda yo‘naltiriladigan URL havolani kiriting', verbose_name='Havola')),
                ('css_class', models.CharField(help_text='Tugmaga qo‘llanadigan CSS class nomini kiriting', max_length=100, verbose_name='CSS Class')),
            ],
            options={
                'verbose_name': '1. Hush kelibsiz tugmalar',
                'verbose_name_plural': '1. Hush kelibsiz tugmalar',
            },
        ),
    ]
