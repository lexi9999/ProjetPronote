# Generated by Django 5.0.6 on 2024-06-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_alter_note_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5),
        ),
    ]
