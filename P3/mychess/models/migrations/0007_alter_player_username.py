# Generated by Django 4.2.2 on 2024-04-06 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0006_alter_chessgame_white'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]