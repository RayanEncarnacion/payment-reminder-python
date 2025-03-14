# Generated by Django 5.1.6 on 2025-03-04 02:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('active', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('createdBy', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('active', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('amount', models.FloatField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payment_reminder.client')),
                ('createdBy', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('due_date', models.DateTimeField()),
                ('amount', models.FloatField()),
                ('payed', models.BooleanField(default=False)),
                ('createdBy', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='payment_reminder.project')),
            ],
            options={
                'db_table': 'payment',
            },
        ),
        migrations.CreateModel(
            name='ProjectDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('day', models.SmallIntegerField()),
                ('createdBy', models.ForeignKey(db_column='created_by', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dates', to='payment_reminder.project')),
            ],
            options={
                'db_table': 'projectDate',
            },
        ),
    ]
