# Generated by Django 4.0.4 on 2022-05-04 19:20

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion_core', '0002_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to='equipe', verbose_name='Imagem'),
        ),
    ]