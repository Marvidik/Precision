# Generated by Django 4.1 on 2022-10-22 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_demo_alter_english_ans_alter_maths_ans'),
    ]

    operations = [
        migrations.CreateModel(
            name='Essay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('essay', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='english',
            name='essay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.essay'),
        ),
    ]
