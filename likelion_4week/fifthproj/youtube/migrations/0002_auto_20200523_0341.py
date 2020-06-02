# Generated by Django 3.0.6 on 2020-05-23 03:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtube',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
        migrations.AddField(
            model_name='youtube',
            name='summary',
            field=models.TextField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='youtube',
            name='text',
            field=models.TextField(default=django.utils.timezone.now, max_length=2000),
            preserve_default=False,
        ),
    ]