# Generated by Django 5.0.4 on 2024-04-24 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2024-04-25 12:00:00'),
            preserve_default=False,
        ),
    ]
