# Generated by Django 4.0.4 on 2022-05-05 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion_core', '0009_recurso_delay'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='lado',
            field=models.ImageField(choices=[('0,3s', '0,3 segundos'), ('0,6s', '0,6 segundos'), ('0,9s', '0,9 segundos')], default=1, max_length=13, upload_to='', verbose_name='Lado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.ImageField(choices=[('lni-laptop-phone', 'Laptop_Phone'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Planta'), ('lni-layers', 'Quadrado'), ('lni-rocket', 'Foquete')], max_length=16, upload_to='', verbose_name='Icone'),
        ),
    ]
