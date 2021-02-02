# Generated by Django 3.1.4 on 2021-01-31 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0004_auto_20210131_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iscedlevel',
            name='ages',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='iscedlevel',
            name='grade',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='programmap',
            name='path',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='institution.iscedlevel'),
        ),
        migrations.AlterField(
            model_name='programmap',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.program'),
        ),
    ]
