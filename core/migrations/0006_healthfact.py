# Generated by Django 5.0.2 on 2024-06-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_healthplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('plan_type', models.CharField(choices=[('nutrition', 'Nutrition'), ('exercise', 'Exercise')], max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='health_facts/')),
            ],
        ),
    ]
