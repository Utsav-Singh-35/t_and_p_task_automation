# Generated by Django 5.1.1 on 2025-01-01 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement_api', '0004_jobapplication_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobacceptance',
            name='salary_category',
            field=models.CharField(default='', max_length=100),
        ),
    ]
