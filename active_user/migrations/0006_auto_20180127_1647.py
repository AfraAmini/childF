# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-27 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active_user', '0005_auto_20180125_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='madadjoo_hamyar_letter',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='madadjoo_madadkar_letter',
            name='thank',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='madadjoo_madadkar_letter',
            name='title',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='hamyar_madadjoo_meeting',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='hamyar_madadjoo_payment',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='hamyar_system_payment',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='madadjoo_hamyar_letter',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='madadjoo_madadkar_letter',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='confirmed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='requirements',
            name='type',
            field=models.CharField(choices=[('mo', 'monthly'), ('ann', 'annual'), ('inst', 'instantly')], default='mo', max_length=60, null=True),
        ),
    ]
