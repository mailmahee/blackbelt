# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('point_one', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='login_reg_app.User')),
                ('point_two', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to='login_reg_app.User')),
            ],
        ),
    ]
