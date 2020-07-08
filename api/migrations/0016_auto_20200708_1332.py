# Generated by Django 3.0.8 on 2020-07-08 05:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_classroom_end_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroomstudent',
            options={'ordering': ['classroom']},
        ),
        migrations.AlterField(
            model_name='classroomstudent',
            name='out_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 8, 5, 32, 29, 855709, tzinfo=utc), verbose_name='退出时间'),
        ),
    ]
