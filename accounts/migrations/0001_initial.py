# Generated by Django 5.2.3 on 2025-06-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('profession', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('user', 'User'), ('persona', 'Persona')], max_length=20)),
                ('specialisation', models.CharField(blank=True, max_length=255, null=True)),
                ('similar_attribute', models.TextField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
