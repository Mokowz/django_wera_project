# Generated by Django 4.2.2 on 2023-08-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='payment',
            field=models.PositiveIntegerField(default=20),
        ),
    ]
