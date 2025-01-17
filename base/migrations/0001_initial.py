# Generated by Django 5.1.1 on 2024-10-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='colege')),
                ('location', models.CharField(max_length=500, verbose_name='location')),
                ('university', models.CharField(max_length=300, verbose_name='university')),
                ('courses', models.CharField(max_length=300, verbose_name='courses')),
                ('ownership', models.CharField(max_length=300, verbose_name='ownership')),
                ('phone_number', models.CharField(max_length=300, verbose_name='phone_number')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
    ]
