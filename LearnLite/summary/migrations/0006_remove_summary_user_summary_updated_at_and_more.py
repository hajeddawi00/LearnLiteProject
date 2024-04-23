# Generated by Django 5.0.1 on 2024-04-23 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0005_alter_summary_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='summary',
            name='user',
        ),
        migrations.AddField(
            model_name='summary',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='summary',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summaries', to='summary.document'),
        ),
    ]