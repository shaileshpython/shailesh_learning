# Generated by Django 2.2 on 2022-11-28 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='job_roles',
        ),
        migrations.AddField(
            model_name='candidate',
            name='job_roles',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='job_role', to='candidate.JobRoles'),
        ),
    ]