# Generated by Django 4.0.5 on 2023-09-07 09:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_comment_options_comment_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]