# Generated by Django 3.1.4 on 2021-01-31 18:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('sunday_start', models.TimeField(blank=True, null=True)),
                ('sunday_end', models.TimeField(blank=True, null=True)),
                ('monday_start', models.TimeField(blank=True, null=True)),
                ('monday_end', models.TimeField(blank=True, null=True)),
                ('tueday_start', models.TimeField(blank=True, null=True)),
                ('tueday_end', models.TimeField(blank=True, null=True)),
                ('wednesday_start', models.TimeField(blank=True, null=True)),
                ('wednesday_end', models.TimeField(blank=True, null=True)),
                ('thursday_start', models.TimeField(blank=True, null=True)),
                ('thursday_end', models.TimeField(blank=True, null=True)),
                ('friday_start', models.TimeField(blank=True, null=True)),
                ('friday_end', models.TimeField(blank=True, null=True)),
                ('saturday_start', models.TimeField(blank=True, null=True)),
                ('saturday_end', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Break',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('start_at', models.TimeField(blank=True, null=True)),
                ('end_at', models.TimeField(blank=True, null=True)),
                ('sunday', models.BooleanField(default=False)),
                ('monday', models.BooleanField(default=False)),
                ('tuesday', models.BooleanField(default=False)),
                ('wednesday', models.BooleanField(default=False)),
                ('thursday', models.BooleanField(default=False)),
                ('friday', models.BooleanField(default=False)),
                ('saturday', models.BooleanField(default=False)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.schedule')),
            ],
        ),
    ]
