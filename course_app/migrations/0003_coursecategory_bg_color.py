# Generated by Django 5.1.3 on 2024-11-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_alter_course_options_alter_coursecategory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursecategory',
            name='bg_color',
            field=models.CharField(default='#', help_text='Orqa fon rangi.', max_length=255, verbose_name='Orqa fon rangi'),
        ),
    ]
