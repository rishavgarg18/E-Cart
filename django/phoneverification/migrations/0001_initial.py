# Generated by Django 2.0 on 2020-08-10 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=50)),
                ('otp', models.CharField(max_length=50)),
                ('auth_id', models.CharField(max_length=500)),
            ],
        ),
    ]