# Generated by Django 5.1.2 on 2024-10-30 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_importer', '0004_remove_activitymap_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitymap',
            name='sequence',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
