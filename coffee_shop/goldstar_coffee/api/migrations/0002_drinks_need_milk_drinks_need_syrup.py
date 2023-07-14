# Generated by Django 4.2.2 on 2023-07-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drinks',
            name='need_milk',
            field=models.BooleanField(default=True, verbose_name='Do you need milk??'),
        ),
        migrations.AddField(
            model_name='drinks',
            name='need_syrup',
            field=models.BooleanField(default=True, verbose_name='Do you need syrup?'),
        ),
    ]