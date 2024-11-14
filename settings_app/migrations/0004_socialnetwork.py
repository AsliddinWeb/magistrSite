# Generated by Django 5.1.3 on 2024-11-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_app', '0003_seosettings_site_css'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Ijtimoiy tarmoq nomi')),
                ('link', models.CharField(max_length=200, verbose_name='Havola')),
                ('i_class', models.CharField(max_length=100, verbose_name='Ikonka klassi')),
            ],
            options={
                'verbose_name': 'Ijtimoiy tarmoq',
                'verbose_name_plural': 'Ijtimoiy tarmoqlar',
            },
        ),
    ]