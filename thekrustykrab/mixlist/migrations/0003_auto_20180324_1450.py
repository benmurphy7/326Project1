# Generated by Django 2.0.2 on 2018-03-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixlist', '0002_auto_20180324_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlistmembership',
            name='time',
            field=models.DurationField(),
        ),
    ]