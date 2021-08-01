# Generated by Django 3.1.7 on 2021-07-29 21:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='image/')),
                ('file', models.FileField(upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
