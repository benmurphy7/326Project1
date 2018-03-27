# Generated by Django 2.0.2 on 2018-03-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixlist', '0003_auto_20180324_1450'),
    ]

    operations = [
        migrations.AddField(
            model_name='mix',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='mix',
            name='like_count',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
