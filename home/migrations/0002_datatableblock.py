# Generated by Django 4.2.4 on 2023-08-24 07:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTableBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_updated', models.DateTimeField(auto_now=True)),
                ('table_data', models.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
