# Generated by Django 5.0.1 on 2024-04-28 18:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_alter_question_correct_answer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='generatedtest',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tests_uploaded', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
