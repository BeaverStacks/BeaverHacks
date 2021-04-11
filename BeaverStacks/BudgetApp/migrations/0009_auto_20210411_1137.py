# Generated by Django 3.2 on 2021-04-11 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BudgetApp', '0008_auto_20210411_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='remaining',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=16),
        ),
        migrations.AddField(
            model_name='categories',
            name='spent',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=16),
        ),
    ]
