# Generated by Django 2.2.5 on 2019-09-21 16:17

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190921_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='languages',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('English', 'English'), ('Germany', 'Germany'), ('French', 'French')], max_length=22),
        ),
    ]
