import factory
from app.models import Tipologia
from test.factories.usuario import UsuarioFactory
from test.factories.setor import SetorFactory
from test.factories.fase import FaseFactory
from test.factories.especieDocumental import EspecieDocumentalFactory


class TipologiaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tipologia
        django_get_or_create = ('nome',)

    setor = factory.SubFactory(SetorFactory)
    usuario = factory.SubFactory(UsuarioFactory)
    especieDocumental = factory.SubFactory(EspecieDocumentalFactory)
    finalidade = factory.Sequence(lambda n: "Finalidade do Documento %03d" % n)
    nome = factory.Sequence(lambda n: "Nome da Tipologia %03d" % n)
    identificacao = factory.Sequence(lambda n: "Identificacao do Documento %03d" % n)

    #To Do: este campo não está sendo criado com sucesso. Verificar esta funcionalidade.
    @factory.post_generation
    def fases(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for fase in extracted:
                self.fases.add(fase)