# Generated by Django 5.1.3 on 2024-11-24 19:33

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_modelconfig_last_trained_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelconfig',
            name='parameters',
            field=models.JSONField(default=core.models.ModelConfig.get_default_params),
        ),
    ]
