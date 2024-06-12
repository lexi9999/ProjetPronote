# Generated by Django 4.1 on 2024-06-12 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enseignant_id', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Calendar Events',
                'verbose_name_plural': 'Calendar Events',
            },
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.eleve')),
                ('enseignant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.enseignant')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Absences.events')),
            ],
            options={
                'verbose_name': 'Absence',
                'verbose_name_plural': 'Absences',
            },
        ),
    ]
