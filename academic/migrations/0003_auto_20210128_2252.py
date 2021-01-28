# Generated by Django 3.1.4 on 2021-01-28 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20210128_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='instructor_course_schedules',
            new_name='instructors',
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='season',
            field=models.CharField(choices=[(None, '(Unknown)'), ('SU', 'Summer'), ('WI', 'Winter'), ('AU', 'Autumn'), ('SP', 'Spring')], max_length=2),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='semester',
            field=models.IntegerField(choices=[(1, '1st Semester'), (2, '2nd Semester'), (3, '3rd Semester')]),
        ),
        migrations.AlterField(
            model_name='academicyear',
            name='type',
            field=models.IntegerField(choices=[(0, 'Semester'), (1, 'Trimester')]),
        ),
    ]
