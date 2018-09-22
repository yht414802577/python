# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('NewClients', models.CharField(max_length=10)),
                ('TotalSales', models.CharField(max_length=10)),
                ('TodayProfit', models.CharField(max_length=10)),
                ('NewInvoice', models.CharField(max_length=10)),
            ],
        ),
    ]
