# Generated by Django 5.1.1 on 2024-12-31 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_backLog',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='is_kt',
            field=models.BooleanField(default=False),
        ),
    ]
