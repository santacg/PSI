# Generated by Django 4.2.2 on 2024-04-06 14:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0010_alter_chessgame_black_alter_chessgame_white'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chessgame',
            name='black',
        ),
        migrations.RemoveField(
            model_name='chessgame',
            name='white',
        ),
        migrations.AddField(
            model_name='chessgame',
            name='blackPlayer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blackPlayer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chessgame',
            name='whitePlayer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='whitePlayer', to=settings.AUTH_USER_MODEL),
        ),
    ]
