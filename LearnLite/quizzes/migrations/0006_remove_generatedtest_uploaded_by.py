# Generated by Django 5.0.1 on 2024-04-28 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0005_generatedtest_uploaded_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedtest',
            name='uploaded_by',
        ),
    ]
