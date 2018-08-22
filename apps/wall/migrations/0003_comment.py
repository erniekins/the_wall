# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-21 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_wall_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall.User')),
                ('wall_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall.Wall_message')),
            ],
        ),
    ]
