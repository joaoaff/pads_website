# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('manual', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('outros_autores', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('cargo', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='publicacao',
            name='autor',
            field=models.ForeignKey(to='pads.Usuario'),
        ),
    ]
