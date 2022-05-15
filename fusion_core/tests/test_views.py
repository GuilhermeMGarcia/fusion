from django.urls import reverse_lazy
from django.test import TestCase, Client


class IndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.dados = {
            'nome': 'Cobra',
            'email': 'cobra@gmail.com',
            'assunto': 'cobra',
            'mensagem': 'cobra'
        }
        self.cliente = Client()

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('fusion_core:index'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_form_invalid(self):
        request = self.cliente.post(reverse_lazy('fusion_core:index'), data=None)
        self.assertEquals(request.status_code, 200)
