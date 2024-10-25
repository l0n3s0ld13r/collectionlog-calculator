# Generated by Django 5.1.2 on 2024-10-25 00:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_updated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('is_updated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='KillCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.IntegerField(default=0)),
                ('sequence', models.IntegerField()),
                ('log_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='killcounts', to='log_importer.logentry')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
                ('obtained', models.BooleanField(default=False)),
                ('sequence', models.IntegerField()),
                ('log_entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='log_importer.logentry')),
            ],
        ),
        migrations.AddField(
            model_name='logentry',
            name='tab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='log_importer.tab'),
        ),
    ]