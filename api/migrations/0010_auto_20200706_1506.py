# Generated by Django 3.0.8 on 2020-07-06 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200706_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-publisher']},
        ),
        migrations.AlterModelOptions(
            name='discuss',
            options={'ordering': ['-pub_time']},
        ),
    ]
