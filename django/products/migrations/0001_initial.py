# Generated by Django 2.0 on 2020-08-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=500)),
                ('price', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=1000)),
            ],
        ),
    ]
