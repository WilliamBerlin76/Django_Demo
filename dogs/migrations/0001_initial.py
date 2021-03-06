# Generated by Django 3.0.5 on 2020-04-16 21:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('breed', models.CharField(max_length=200)),
                ('weight', models.IntegerField()),
            ],
        ),
    ]
