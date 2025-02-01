# Generated by Django 5.1.5 on 2025-02-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dlc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название длс')),
                ('cost', models.DecimalField(decimal_places=3, max_digits=20, verbose_name='Цена')),
                ('size', models.DecimalField(decimal_places=3, max_digits=30)),
                ('description', models.TextField(blank=True)),
                ('age_limited', models.BooleanField(default=False)),
            ],
        ),
    ]
