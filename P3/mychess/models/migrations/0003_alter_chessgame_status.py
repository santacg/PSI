# Generated by Django 4.2.2 on 2024-04-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0002_alter_chessgame_black_player_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chessgame',
            name='status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('ACTIVE', 'active'), ('FINISHED', 'finished')], default='PENDING', max_length=64),
        ),
    ]
