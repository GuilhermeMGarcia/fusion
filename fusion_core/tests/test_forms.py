from django.test import TestCase
from model_mommy import mommy

from fusion_core.forms import ContatoForm


class ContatoFormTestCase(TestCase):

    def setUp(self) -> None:
        self.nome = 'Cobra'
        self.email = 'cobra@gmail.com'
        self.assunto = 'cobra'
        self.mensagem = 'cobra'

        self.conteudo = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem
        }

    def test_send_mail(self):
        form1 = ContatoForm(data=self.conteudo)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = ContatoForm(data=self.conteudo)
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)
