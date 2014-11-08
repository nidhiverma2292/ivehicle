# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=6, choices=[(b'se', b'Sedan'), (b'su', b'SUV'), (b'ha', b'HashBack')])),
                ('ac', models.BooleanField(default=True)),
                ('rent', models.IntegerField()),
                ('image', models.ImageField(upload_to=b'/car/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
