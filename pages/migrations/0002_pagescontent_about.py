# Generated by Django 3.2.7 on 2021-09-05 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagescontent',
            name='about',
            field=models.TextField(default='about'),
            preserve_default=False,
        ),
    ]