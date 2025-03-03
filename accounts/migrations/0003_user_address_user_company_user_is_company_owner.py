# Generated by Django 5.0.7 on 2024-08-30 16:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_phone_number'),
        ('job_recruitment', '0005_jobcategory_remove_jobseeker_user_job_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='job_recruitment.company'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_company_owner',
            field=models.BooleanField(default=False),
        ),
    ]
