# Generated by Django 3.2 on 2022-04-04 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kv_app', '0002_remove_projectusers_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='auditorya',
            field=models.CharField(blank=True, choices=[('Пусто', 'Пусто'), ('Ақпараттық орталық', 'Ақпараттық орталық'), ('Г-301', 'Г-301'), ('Г-306', 'Г-306'), ('Г-204', 'Г-204'), ('Г-205', 'Г-205'), ('Г-202', 'Г-202'), ('Г-207', 'Г-207'), ('Г-208', 'Г-208'), ('Г-211', 'Г-211'), ('Г-212', 'Г-212'), ('ФМ-202', 'ФМ-202'), ('ФМ-201', 'ФМ-201'), ('ФМ-104', 'ФМ-104'), ('ФМ-101', 'ФМ-101'), ('ХБ-101', 'ХБ-101'), ('Т-101', 'Т-101'), ('Т-102', 'Т-102'), ('Т-103', 'Т-103'), ('Т-104', 'Т-104'), ('Кітапхана', 'Кітапхана')], default='Пусто', max_length=100, null=True, verbose_name='Аудитория'),
        ),
    ]
