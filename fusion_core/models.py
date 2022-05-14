from uuid import uuid4
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid4()}{ext}'
    return filename


class Base(models.Model):
    criado = models.DateField('Criado', auto_now_add=True)
    editado = models.DateField('Editado', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Trab(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafico'),
        ('lni-users', 'Usuarios'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foquete')
    )

    trab = models.CharField('Trabs', max_length=100)
    descricao = models.TextField('Descriçao', max_length=200)
    icone = models.ImageField('Icone', max_length=12, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Trab'
        verbose_name_plural = 'Trabs'

    def __str__(self):
        return self.trab


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('fusion_core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=250)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480,
                                                                                    'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        return self.nome


class RecursoDireita(Base):
    ICONE_CHOICES = (
        ('lni-laptop-phone', 'Laptop_Phone'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Planta'),
        ('lni-layers', 'Quadrado'),
        ('lni-rocket', 'Foquete')
    )
    DELAY_CHOICES = (
        ('0.3s', '0,3 segundos'),
        ('0.6s', '0,6 segundos'),
        ('0.9s', '0,9 segundos')
    )

    recurso_direita = models.CharField('Recurso Direita', max_length=100)
    descricao = models.TextField('Descriçao', max_length=200)
    icone = models.ImageField('Icone', max_length=16, choices=ICONE_CHOICES)
    delay = models.ImageField('Delay', max_length=4, choices=DELAY_CHOICES)

    class Meta:
        verbose_name = 'recurso_direita'
        verbose_name_plural = 'recursos_direita'

    def __str__(self):
        return self.recurso_direita


class RecursoEsquerda(Base):
    ICONE_CHOICES = (
        ('lni-laptop-phone', 'Laptop_Phone'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Planta'),
        ('lni-layers', 'Quadrado'),
        ('lni-rocket', 'Foquete')
    )
    DELAY_CHOICES = (
        ('0.3s', '0,3 segundos'),
        ('0.6s', '0,6 segundos'),
        ('0.9s', '0,9 segundos')
    )

    recurso_esquerda = models.CharField('Recurso Esquerda', max_length=100)
    descricao = models.TextField('Descriçao', max_length=200)
    icone = models.ImageField('Icone', max_length=16, choices=ICONE_CHOICES)
    delay = models.ImageField('Delay', max_length=4, choices=DELAY_CHOICES)

    class Meta:
        verbose_name = 'recurso_esquerda'
        verbose_name_plural = 'recursos_esquerda'

    def __str__(self):
        return self.recurso_esquerda


class Precos(Base):
    ICONE_CHOICES = (
        ('lni-package', 'caixa'),
        ('lni-drop', 'gota de agua'),
        ('lni-star', 'estrela'),
    )

    preco = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    nome = models.CharField('Titulo', max_length=100)
    icone = models.ImageField('Icone', max_length=11, choices=ICONE_CHOICES)
    description_1 = models.CharField('Descriçao 1', max_length=100)
    description_2 = models.CharField('Descriçao 2', max_length=100)
    description_3 = models.CharField('Descriçao 3', max_length=100)
    description_4 = models.CharField('Descriçao 4', max_length=100)

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return self.nome
