# Generated by Django 4.1.3 on 2022-11-16 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=12)),
                ('phone', models.CharField(max_length=12)),
                ('is_created_date', models.DateField(auto_now_add=True)),
                ('is_created_time', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
