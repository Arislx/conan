# Generated by Django 2.1 on 2019-05-05 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_group_people_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestgrade',
            name='is_simulation',
            field=models.BooleanField(default=False, verbose_name='是否模拟'),
        ),
    ]
