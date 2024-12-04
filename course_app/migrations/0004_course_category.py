# Generated by Django 5.1.3 on 2024-11-14 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0003_coursecategory_bg_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='course_app.coursecategory', verbose_name='Kategoriya'),
            preserve_default=False,
        ),
    ]
