# Generated by Django 3.2 on 2021-04-10 23:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BudgetApp', '0004_auto_20210410_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgets',
            name='month',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='budgets',
            name='year',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
