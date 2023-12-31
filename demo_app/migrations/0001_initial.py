# Generated by Django 4.0 on 2023-01-05 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_Name', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('product_stock', models.IntegerField()),
                ('img_url', models.CharField(max_length=200)),
                ('product_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
