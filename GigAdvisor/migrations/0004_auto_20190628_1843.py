# Generated by Django 2.2 on 2019-06-28 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GigAdvisor', '0003_platform_recensioni'),
    ]

    operations = [
        migrations.AddField(
            model_name='recensioni',
            name='sicurezza',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recensioni',
            name='data',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='recensioni',
            name='platform',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='GigAdvisor.Platform'),
            preserve_default=False,
        ),
    ]
