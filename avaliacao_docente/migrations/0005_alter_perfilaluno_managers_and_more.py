# Generated by Django 5.2.1 on 2025-07-17 01:33

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao_docente', '0004_alter_perfilaluno_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='perfilaluno',
            managers=[
                ('non_admin', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='perfilprofessor',
            managers=[
                ('non_admin', django.db.models.manager.Manager()),
            ],
        ),
    ]
