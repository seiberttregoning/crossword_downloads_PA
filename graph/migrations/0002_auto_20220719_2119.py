# Generated by Django 3.2.3 on 2022-07-20 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solve',
            name='solve_Seconds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='solve',
            name='solve_Time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]