# Generated by Django 2.2 on 2019-07-02 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GigAdvisor', '0009_auto_20190702_0954'),
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
