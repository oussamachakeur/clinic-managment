# Generated by Django 3.2.25 on 2025-04-15 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20250414_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='receptionist',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='receptionist_reviewed', to='core.receptionist'),
        ),
    ]
