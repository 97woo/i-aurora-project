# Generated by Django 4.0.3 on 2022-04-15 10:04

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('identification', models.CharField(max_length=100, unique=True)),
                ('point', models.PositiveIntegerField(default=1000000)),
                ('card_number', models.CharField(max_length=50, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'users',
            },
            managers=[
                ('objects', users.models.UserManager()),
            ],
        ),
    ]
