# Generated by Django 2.0.2 on 2018-04-16 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixlist', '0008_auto_20180412_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mix',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mix',
            name='play_count',
            field=models.IntegerField(default=0),
        ),
    ]
