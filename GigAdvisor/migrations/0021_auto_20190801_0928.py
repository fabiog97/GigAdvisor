# Generated by Django 2.2 on 2019-08-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GigAdvisor', '0020_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='titolo_di_studio',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
