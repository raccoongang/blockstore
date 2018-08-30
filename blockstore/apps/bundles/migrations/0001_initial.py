# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-10 22:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('title', models.CharField(db_index=True, max_length=180)),
                ('slug', models.SlugField(allow_unicode=True)),
                ('description', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='BundleLink',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uses_latest', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BundleVersion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('version_num', models.PositiveIntegerField()),
                ('snapshot_digest', models.BinaryField(db_index=True, max_length=20)),
                ('change_description', models.TextField(blank=True, max_length=1000)),
                ('bundle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', related_query_name='version', to='bundles.Bundle')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('title', models.CharField(db_index=True, max_length=180)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='bundleversion',
            unique_together=set([('bundle', 'version_num')]),
        ),
    ]