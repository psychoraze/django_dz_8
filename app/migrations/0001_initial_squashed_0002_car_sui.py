# Generated by Django 5.0.2 on 2024-02-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('app', '0001_initial'), ('app', '0002_car_sui')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wheels', models.IntegerField()),
                ('volume', models.IntegerField()),
                ('color', models.CharField(max_length=255)),
                ('seats', models.IntegerField()),
                ('producer', models.CharField(default=1, max_length=255)),
                ('v_or_i', models.IntegerField(default=1, max_length=255)),
                ('sui', models.IntegerField(default=1)),
            ],
        ),
    ]
