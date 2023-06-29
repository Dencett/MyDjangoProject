# Generated by Django 4.1.7 on 2023-05-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_alter_housing_options_alter_housingtype_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='published_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='housing',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]