# Generated by Django 2.2.4 on 2022-03-25 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20220321_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='moderator',
            field=models.BooleanField(default=False),
        ),
    ]
