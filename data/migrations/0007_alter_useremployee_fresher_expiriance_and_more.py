# Generated by Django 4.0.1 on 2022-02-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_alter_useremployee_per_12th'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremployee',
            name='fresher_expiriance',
            field=models.CharField(choices=[(1, 'Fresher'), (2, 'Experience')], max_length=24),
        ),
        migrations.AlterField(
            model_name='useremployee',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]
