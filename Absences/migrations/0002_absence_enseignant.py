# Generated by Django 4.1 on 2024-06-10 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_enseignant_id'),
        ('Absences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='absence',
            name='enseignant',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='User.enseignant'),
            preserve_default=False,
        ),
    ]
