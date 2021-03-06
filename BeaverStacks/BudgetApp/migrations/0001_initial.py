# Generated by Django 3.2 on 2021-04-10 05:36

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budgets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('spent', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('remaining', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
                ('year', models.DateTimeField(default=2021)),
                ('month', models.DateField(default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=16)),
            ],
        ),
        migrations.CreateModel(
            name='UserTransactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BudgetApp.categories')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BudgetApp.groups')),
                ('transaction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BudgetApp.transactions')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserBudget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BudgetApp.budgets')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BudgetApp.categories')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BudgetApp.groups')),
            ],
        ),
    ]
