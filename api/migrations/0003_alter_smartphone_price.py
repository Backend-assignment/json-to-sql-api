# Generated by Django 4.1.7 on 2023-03-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_smartphone_color_alter_smartphone_img_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='price',
            field=models.FloatField(),
        ),
    ]
