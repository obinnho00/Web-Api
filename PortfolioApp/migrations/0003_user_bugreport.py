# Generated by Django 5.1.4 on 2024-12-16 08:57

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioApp', '0002_remove_aboutme_fun_interests'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BugReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('bug_type', models.CharField(max_length=50)),
                ('report', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bug_reports', to='PortfolioApp.user')),
            ],
            options={
                'verbose_name': 'Bug Report',
                'verbose_name_plural': 'Bug Reports',
                'db_table': 'bug_report',
                'managed': True,
            },
        ),
    ]
