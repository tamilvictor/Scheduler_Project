# Generated by Django 5.1 on 2024-08-10 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('job_type', models.CharField(choices=[('email_notification', 'Email Notification'), ('number_crunching', 'Number Crunching'), ('data_backup', 'Data Backup')], max_length=50)),
                ('interval', models.IntegerField()),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('next_run', models.DateTimeField(blank=True, null=True)),
                ('parameters', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
