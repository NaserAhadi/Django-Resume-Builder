# Generated by Django 2.2.5 on 2019-09-19 09:38

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190919_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='mobilephone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
