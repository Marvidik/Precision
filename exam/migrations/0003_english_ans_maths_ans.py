# Generated by Django 4.1 on 2022-10-09 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_english_maths_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='english',
            name='ans',
            field=models.CharField(default='3', max_length=100),
        ),
        migrations.AddField(
            model_name='maths',
            name='ans',
            field=models.CharField(default='3', max_length=100),
        ),
    ]