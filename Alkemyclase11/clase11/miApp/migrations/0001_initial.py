# Generated by Django 5.0.3 on 2024-03-15 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(max_length=100)),
                ('descripción', models.CharField(max_length=100)),
                ('categoría', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('precio', models.IntegerField(max_length=7)),
            ],
        ),
    ]
