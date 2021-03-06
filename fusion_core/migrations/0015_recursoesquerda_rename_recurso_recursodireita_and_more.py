# Generated by Django 4.0.4 on 2022-05-05 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusion_core', '0014_alter_recurso_delay'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoEsquerda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('editado', models.DateField(auto_now=True, verbose_name='Editado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('recurso_esquerda', models.CharField(max_length=100, verbose_name='Recurso')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descriçao')),
                ('icone', models.ImageField(choices=[('lni-laptop-phone', 'Laptop_Phone'), ('lni-cog', 'Engrenagem'), ('lni-leaf', 'Planta'), ('lni-layers', 'Quadrado'), ('lni-rocket', 'Foquete')], max_length=16, upload_to='', verbose_name='Icone')),
                ('delay', models.ImageField(choices=[('0.3s', '0,3 segundos'), ('0.6s', '0,6 segundos'), ('0.9s', '0,9 segundos')], max_length=4, upload_to='', verbose_name='Delay')),
            ],
            options={
                'verbose_name': 'recurso_esquerda',
                'verbose_name_plural': 'recurso_esquerda',
            },
        ),
        migrations.RenameModel(
            old_name='Recurso',
            new_name='RecursoDireita',
        ),
        migrations.AlterModelOptions(
            name='recursodireita',
            options={'verbose_name': 'recurso_direita', 'verbose_name_plural': 'recursos_direita'},
        ),
        migrations.RenameField(
            model_name='recursodireita',
            old_name='recurso',
            new_name='recurso_direita',
        ),
    ]
