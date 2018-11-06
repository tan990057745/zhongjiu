# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('saleNum', models.IntegerField()),
                ('commentsNum', models.CharField(max_length=100)),
                ('isxf', models.IntegerField()),
                ('isspec', models.IntegerField()),
                ('brandid', models.IntegerField()),
                ('placeid', models.IntegerField()),
                ('priceid', models.IntegerField()),
                ('suitid', models.IntegerField()),
                ('sortid', models.IntegerField()),
                ('shelfTime', models.DateField()),
            ],
            options={
                'db_table': 'zj_supermarket',
            },
        ),
    ]
