# Generated by Django 2.2 on 2019-08-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GigAdvisor', '0022_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/default.png', upload_to='avatar/'),
        ),
    ]
