# Generated by Django 4.0.7 on 2022-08-25 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spark', '0005_event'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='EventCategory',
        ),
        migrations.DeleteModel(
            name='EventProvider',
        ),
    ]
