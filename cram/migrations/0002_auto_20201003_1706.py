# Generated by Django 3.1.2 on 2020-10-03 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='regex_country',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='page',
            name='regex_time',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='page',
            name='xpath_country',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='page',
            name='xpath_time',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
