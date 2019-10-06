# Generated by Django 2.2.5 on 2019-09-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190921_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_info',
            name='graduation',
            field=models.CharField(blank=True, max_length=20, verbose_name='Graduation '),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='major',
            field=models.CharField(blank=True, max_length=20, verbose_name='Major '),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='university',
            field=models.CharField(blank=True, max_length=20, verbose_name='University '),
        ),
        migrations.AlterField(
            model_name='personal_info',
            name='degrees',
            field=models.CharField(blank=True, max_length=20, verbose_name='Degrees '),
        ),
    ]