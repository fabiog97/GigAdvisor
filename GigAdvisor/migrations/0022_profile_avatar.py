# Generated by Django 2.2 on 2019-08-01 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GigAdvisor', '0021_auto_20190801_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='avatar/default.png', upload_to='avatar'),
        ),
    ]
