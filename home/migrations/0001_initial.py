# Generated by Django 4.1.3 on 2023-08-12 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InternApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desired_domain', models.CharField(choices=[('web', 'Web Development'), ('app', 'App Development'), ('ml', 'Machine Learning')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('qualification', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
