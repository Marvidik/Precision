# Generated by Django 4.1 on 2022-10-09 14:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='English',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('essay', models.TextField()),
                ('Quest', models.TextField()),
                ('op1', models.CharField(max_length=100)),
                ('op2', models.CharField(max_length=100)),
                ('op3', models.CharField(max_length=100)),
                ('op4', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Maths',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quest', models.TextField()),
                ('op1', models.CharField(max_length=100)),
                ('op2', models.CharField(max_length=100)),
                ('op3', models.CharField(max_length=100)),
                ('op4', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('score', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]