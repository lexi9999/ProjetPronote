# Generated by Django 4.2.7 on 2024-06-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENSISmart', '0011_alter_eleve_password_alter_enseignant_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='eleve',
            name='is_first_co',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='enseignant',
            name='is_first_co',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='eleve',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='enseignant',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
