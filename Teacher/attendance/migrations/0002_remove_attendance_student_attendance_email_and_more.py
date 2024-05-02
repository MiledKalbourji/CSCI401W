# Generated by Django 4.1.13 on 2024-05-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='student',
        ),
        migrations.AddField(
            model_name='attendance',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='attendance',
            name='phone_number',
            field=models.CharField(default='000-000-0000', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_id',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='student_name',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='time',
            field=models.CharField(default='00:00', max_length=10),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
