# Generated by Django 5.0.6 on 2024-06-10 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bjjorganizer', '0002_alter_match_match_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='tournamentType',
            field=models.CharField(choices=[('freeforall', 'Free for All'), ('singleelimination', 'Single Elimination'), ('doubleelimination', 'Double Elimination')], default='freeforall', max_length=100),
            preserve_default=False,
        ),
    ]
