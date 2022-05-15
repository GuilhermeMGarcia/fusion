from uuid import uuid4
from django.test import TestCase
from model_mommy import mommy

from fusion_core import models


class GetFilePathTestCase(TestCase):

    def setUp(self) -> None:
        self.filename = f'{uuid4()}.png'

    def test_get_file_path(self):
        arq = models.get_file_path(None, 'test.png')
        self.assertTrue(len(arq), len(self.filename))


class TrabTestCase(TestCase):

    def setUp(self) -> None:
        self.trab = mommy.make('Trab')

    def test_trab(self):
        self.assertEquals(str(self.trab), self.trab.trab)


class CargoTestCase(TestCase):

    def setUp(self) -> None:
        self.cargo = mommy.make('Cargo')

    def test_cargo(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class FuncionarioTestCase(TestCase):

    def setUp(self) -> None:
        self.funcionario = mommy.make('Funcionario')

    def test_funcionario(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)


class RecursoDireitaTestCase(TestCase):

    def setUp(self) -> None:
        self.recurso_d = mommy.make('RecursoDireita')

    def test_recurso_direita(self):
        self.assertEquals(str(self.recurso_d), self.recurso_d.recurso_direita)


class RecursoEsquerdaTestCase(TestCase):

    def setUp(self) -> None:
        self.recurso_e = mommy.make('RecursoEsquerda')

    def test_recurso_esquerda(self):
        self.assertEquals(str(self.recurso_e), self.recurso_e.recurso_esquerda)


class PrecosTestCase(TestCase):

    def setUp(self) -> None:
        self.preco = mommy.make('Precos')

    def test_precos(self):
        self.assertEquals(str(self.preco), self.preco.nome)
