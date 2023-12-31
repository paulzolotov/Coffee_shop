# Generated by Django 4.2.2 on 2023-07-13 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_drinks_price_alter_food_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drinks',
            name='image',
            field=models.FileField(default='settings.MEDIA_ROOT/api/coffee.webp', upload_to='api/'),
        ),
        migrations.AlterField(
            model_name='drinks',
            name='need_milk',
            field=models.BooleanField(default=True, verbose_name='Do you need milk?'),
        ),
    ]
