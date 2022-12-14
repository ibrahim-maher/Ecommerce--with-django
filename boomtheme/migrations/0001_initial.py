# Generated by Django 4.0.7 on 2022-09-11 07:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image1', models.ImageField(upload_to='media_imgs')),
                ('image2', models.ImageField(upload_to='media_imgs')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('total_quantity', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='order_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boomtheme.orders')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boomtheme.products')),
            ],
            options={
                'db_table': 'order_products',
            },
        ),
    ]
