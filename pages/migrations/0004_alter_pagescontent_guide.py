# Generated by Django 3.2.7 on 2021-09-12 07:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210905_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagescontent',
            name='guide',
            field=ckeditor.fields.RichTextField(),
        ),
    ]