# Generated by Django 4.1.7 on 2023-03-07 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmartPhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.TextField()),
                ('img_url', models.TextField()),
                ('color', models.TextField()),
                ('ram', models.TextField()),
                ('memory', models.TextField()),
                ('name', models.TextField()),
                ('model', models.TextField()),
            ],
        ),
    ]
