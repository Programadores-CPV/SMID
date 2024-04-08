# Generated by Django 5.0.3 on 2024-04-03 16:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0008_alter_historicalpiso_name_alter_historicaltorre_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpiso',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='historicaltorre',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='piso',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='torre',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Nombre'),
        ),
        migrations.AddConstraint(
            model_name='torre',
            constraint=models.UniqueConstraint(condition=models.Q(('status', True)), fields=('name',), name='unique_if_status_not_false'),
        ),
    ]
