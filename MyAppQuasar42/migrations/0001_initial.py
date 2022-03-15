# Generated by Django 4.0.2 on 2022-03-11 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.IntegerField(max_length=30)),
                ('field_number', models.IntegerField(max_length=10)),
            ],
        ),
    ]
