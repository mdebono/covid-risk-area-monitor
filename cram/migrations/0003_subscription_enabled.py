# Generated by Django 3.1.2 on 2020-10-03 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cram', '0002_auto_20201003_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
    ]
