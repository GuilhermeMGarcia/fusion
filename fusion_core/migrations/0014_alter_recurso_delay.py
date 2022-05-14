# Generated by Django 4.0.4 on 2022-05-05 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion_core', '0013_alter_recurso_delay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='delay',
            field=models.ImageField(choices=[('0.3s', '0,3 segundos'), ('0.6s', '0,6 segundos'), ('0.9s', '0,9 segundos')], max_length=4, upload_to='', verbose_name='Delay'),
        ),
    ]