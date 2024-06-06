# Generated by Django 4.1 on 2024-06-04 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ENSISmart', '0004_events_vie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Absence',
                'verbose_name_plural': 'Absences',
            },
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Events_vie',
        ),
        migrations.AddField(
            model_name='absence',
            name='eleve',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ENSISmart.eleve'),
        ),
        migrations.AddField(
            model_name='absence',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ENSISmart.events'),
        ),
    ]