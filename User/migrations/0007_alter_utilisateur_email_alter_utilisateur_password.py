# Generated by Django 5.0.6 on 2024-06-06 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_note_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='password',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
