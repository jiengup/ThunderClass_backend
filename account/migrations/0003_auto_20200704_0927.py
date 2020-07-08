# Generated by Django 3.0.8 on 2020-07-04 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200703_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='belong_to_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_to_class', to='account.Class', verbose_name='所在班级'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='null', max_length=20, verbose_name='昵称'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('TC', 'Teacher'), ('ST', 'Student')], default='ST', max_length=10, verbose_name='用户类别'),
        ),
    ]
