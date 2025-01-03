# Generated by Django 5.1.3 on 2024-11-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0008_aboutteam'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('svg', models.TextField(verbose_name='SVG')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('description', models.TextField(verbose_name='Tavsif')),
            ],
            options={
                'verbose_name': '7. Natijalar',
                'verbose_name_plural': '7. Natijalar',
            },
        ),
    ]
