# Generated by Django 2.2 on 2019-07-02 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GigAdvisor', '0008_auto_20190701_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recensioni',
            name='value1',
        ),
        migrations.RemoveField(
            model_name='recensioni',
            name='value2',
        ),
        migrations.RemoveField(
            model_name='recensioni',
            name='value3',
        ),
        migrations.RemoveField(
            model_name='recensioni',
            name='value4',
        ),
    ]
