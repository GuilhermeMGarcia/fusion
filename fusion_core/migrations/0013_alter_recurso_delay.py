# Generated by Django 4.0.4 on 2022-05-05 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion_core', '0012_remove_recurso_lado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='delay',
            field=models.ImageField(choices=[('0,3s', '0,3 segundos'), ('0,6s', '0,6 segundos'), ('3s', '0,9 segundos')], max_length=4, upload_to='', verbose_name='Delay'),
        ),
    ]
