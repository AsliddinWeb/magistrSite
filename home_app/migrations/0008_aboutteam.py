# Generated by Django 5.1.3 on 2024-11-23 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0007_aboutwelcome'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Sarlavha')),
                ('cap_title', models.CharField(max_length=255, verbose_name='Qisqa sarlavha')),
                ('description', models.TextField(verbose_name='Tavsif')),
                ('image', models.ImageField(blank=True, null=True, upload_to='about_team/', verbose_name='Rasm')),
            ],
            options={
                'verbose_name': '6. Jamoadagi kishilar',
                'verbose_name_plural': '6. Jamoadagi kishilar',
            },
        ),
    ]