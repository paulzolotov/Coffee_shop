# Generated by Django 4.2.2 on 2023-07-13 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_drinks_category_of_sort_drink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category_of_sort_food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.varietyinfoodcategory', verbose_name='Variety In Food Category'),
        ),
    ]
