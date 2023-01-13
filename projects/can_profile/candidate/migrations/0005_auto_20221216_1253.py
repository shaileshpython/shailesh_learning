# Generated by Django 2.2 on 2022-12-16 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0004_auto_20221128_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentActivitybkTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('full_name', models.CharField(default='', max_length=150)),
                ('supervisor_name', models.CharField(default='', max_length=150)),
                ('campaign', models.CharField(default='', max_length=150)),
                ('app_idle_time', models.TimeField(blank=True, default=datetime.time(0, 0), null=True)),
                ('dialer_idle_time', models.TimeField(blank=True, default=datetime.time(0, 0), null=True)),
                ('pause_progressive_time', models.TimeField(blank=True, default=datetime.time(0, 0), null=True)),
                ('progressive_time', models.TimeField(blank=True, default=datetime.time(0, 0), null=True)),
                ('preview_time', models.TimeField(blank=True, default=datetime.time(0, 0), null=True)),
                ('ring_duration_avg', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(db_index=True, default=None, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='JobRoles',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(db_index=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='username',
            field=models.CharField(db_index=True, default='admin', max_length=20, unique=True),
        ),
    ]
