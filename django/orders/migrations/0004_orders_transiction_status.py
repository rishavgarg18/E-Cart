# Generated by Django 2.0 on 2020-08-18 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200818_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='transiction_status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]