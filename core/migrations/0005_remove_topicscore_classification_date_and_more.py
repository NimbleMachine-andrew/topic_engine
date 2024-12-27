# Generated by Django 5.1.3 on 2024-11-24 19:12

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_content_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicscore',
            name='classification_date',
        ),
        migrations.RemoveField(
            model_name='topicscore',
            name='classifier_version',
        ),
        migrations.CreateModel(
            name='ModelConfig',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('parameters', models.JSONField(default=dict)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.topic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TopicPrediction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('result', models.CharField(max_length=50)),
                ('confidence', models.FloatField(blank=True, null=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.content')),
                ('model_config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelconfig')),
            ],
            options={
                'indexes': [models.Index(fields=['result', 'confidence'], name='core_topicp_result_9fc9f9_idx')],
                'unique_together': {('content', 'model_config')},
            },
        ),
    ]
