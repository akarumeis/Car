# Generated by Django 4.1.4 on 2023-02-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='image/%Y/%m/%d')),
                ('mark_name', models.CharField(max_length=255)),
                ('model_name', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('fuel', models.CharField(max_length=255)),
                ('weight', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('text', models.TextField(max_length=3000)),
            ],
        ),
    ]