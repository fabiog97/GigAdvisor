# Generated by Django 2.2 on 2019-07-01 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GigAdvisor', '0007_auto_20190701_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='recensioni',
            name='value1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recensioni',
            name='value2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recensioni',
            name='value3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recensioni',
            name='value4',
            field=models.IntegerField(default=0),
        ),
    ]