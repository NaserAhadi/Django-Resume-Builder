# Generated by Django 2.2.5 on 2019-09-19 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_delete_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_info',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]