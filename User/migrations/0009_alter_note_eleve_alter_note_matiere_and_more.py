# Generated by Django 5.0.6 on 2024-06-06 13:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_alter_note_eleve_alter_note_matiere_alter_note_note_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='eleve',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='User.eleve'),
        ),
        migrations.AlterField(
            model_name='note',
            name='matiere',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
