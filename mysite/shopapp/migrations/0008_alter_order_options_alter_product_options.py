# Generated by Django 4.1.7 on 2023-05-19 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0007_alter_product_options_product_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['user'], 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'price'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]
