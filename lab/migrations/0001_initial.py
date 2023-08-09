# Generated by Django 4.1.3 on 2023-08-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LabExperiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard', models.CharField(choices=[('10th', 'Class 10th'), ('12th', 'Class 12th'), ('engineering', 'Engineering')], max_length=20)),
                ('subject', models.CharField(choices=[('physics', 'Physics'), ('chemistry', 'Chemistry'), ('maths', 'Mathematics'), ('electronics', 'Electronics'), ('mechanical', 'Mechanical'), ('civil', 'Civil')], max_length=20)),
                ('experiment', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('experiment_url', models.CharField(max_length=100)),
                ('experiment_css_url', models.CharField(max_length=100)),
            ],
        ),
    ]