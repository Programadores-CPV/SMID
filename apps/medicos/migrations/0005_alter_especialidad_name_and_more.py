# Generated by Django 5.0.3 on 2024-04-03 16:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicos', '0004_alter_especialidad_name_and_more'),
        ('ubicaciones', '0010_remove_torre_unique_if_status_not_false_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='especialidad',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='historicalespecialidad',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='historicalmedico',
            name='code',
            field=models.CharField(max_length=5, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='historicalmedico',
            name='identification',
            field=models.CharField(max_length=9, verbose_name='Cédula de identidad'),
        ),
        migrations.AlterField(
            model_name='historicalmedico',
            name='rif',
            field=models.CharField(max_length=10, verbose_name='RIF'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='code',
            field=models.CharField(max_length=5, verbose_name='Codigo'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='identification',
            field=models.CharField(max_length=9, verbose_name='Cédula de identidad'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='rif',
            field=models.CharField(max_length=10, verbose_name='RIF'),
        ),
        migrations.AddConstraint(
            model_name='especialidad',
            constraint=models.UniqueConstraint(condition=models.Q(('status', True)), fields=('name',), name='specialty_name_unique_if_status_not_false'),
        ),
        migrations.AddConstraint(
            model_name='medico',
            constraint=models.UniqueConstraint(condition=models.Q(('status', True)), fields=('code', 'identification', 'rif'), name='medic_unique_if_status_not_false'),
        ),
    ]
