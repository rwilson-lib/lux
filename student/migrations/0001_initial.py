# Generated by Django 3.1.4 on 2021-01-26 13:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '0002_auto_20210126_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.personal')),
            ],
        ),
    ]
