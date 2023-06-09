# Generated by Django 4.1.3 on 2023-06-05 07:22

import django.core.validators
from django.db import migrations, models
import my_music_app.accounts.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2, 'the field must contain at least 50 characters'), my_music_app.accounts.models.validate_password])),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
    ]
