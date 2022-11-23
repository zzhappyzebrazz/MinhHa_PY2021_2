# Generated by Django 4.1.2 on 2022-11-12 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='image',
            field=models.ImageField(default='stories/images/logo.jpg', upload_to='stories/images'),
        ),
        migrations.AddField(
            model_name='story',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='viewed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='story',
            name='public_day',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]