# Generated by Django 5.1.2 on 2024-11-05 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0004_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comp.product')),
            ],
        ),
    ]
