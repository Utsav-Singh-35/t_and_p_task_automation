# Generated by Django 5.1.1 on 2024-12-31 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_card_student_contact_student_dob_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cgpa',
            field=models.FloatField(null=True),
        ),
    ]
