# Generated by Django 5.1.6 on 2025-03-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_reminder', '0002_update_foreign_key_column_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
