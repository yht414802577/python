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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('DakotaRiceSalary', models.CharField(max_length=10)),
                ('MinervaHooperSalary', models.CharField(max_length=10)),
            ],
        ),
    ]
