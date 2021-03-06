# Generated by Django 4.0.3 on 2022-04-15 10:04

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
            name='Send',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('bankcode', models.IntegerField()),
                ('fee', models.IntegerField(default=500)),
                ('remittor', models.CharField(max_length=20)),
                ('recipient', models.CharField(max_length=20)),
                ('account_no', models.CharField(max_length=40)),
                ('bank_name', models.CharField(max_length=20)),
                ('memo', models.CharField(max_length=30)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='senduser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sends',
            },
        ),
    ]
