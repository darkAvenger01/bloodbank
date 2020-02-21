# Generated by Django 3.0.3 on 2020-02-21 09:45

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',models.CharField(max_length=100)),
                ('email',models.CharField(max_length=100)),
                ('password',models.CharField(max_length=250)),
                ('created_at',models.DateTimeField(default=timezone.now)),
            ],
        ),
    ]
