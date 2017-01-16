from django import forms
from django.forms import ModelForm, Select, TextInput, EmailInput, ChoiceField, CharField, EmailInput,RadioSelect, ModelMultipleChoiceField, SelectMultiple
from .models import *
from django.contrib.auth.models import User


class FormAtividade(ModelForm):
    class Meta:
        model = Atividade
        fields = ['setor', 'descricao']


class FormSetor(ModelForm):
    class Meta:
        model = Setor
        fields = ['campus', 'nome', 'sigla', 'funcao', 'historico']
        widgets = {
            'campus': Select(attrs={'id':'id-campus','class':'browser-default selectField'}),
             'nome': TextInput(attrs={'class':'validate'})
                    }
class FormCampus(ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']


class FormTipologia(ModelForm):
    def __init__(self, *args, **kwargs):
        setor = kwargs.pop('setor', None)
        super(FormTipologia, self).__init__(*args,**kwargs)
        self.fields['atividade'] = forms.ModelChoiceField(required=True, queryset=Atividade.objects.filter(setor=setor), widget=forms.Select())
        self.fields['producaoSetor'].required = True
        self.fields['formaDocumental'].required = True
        self.fields['quantidadeVias'].required = True
        self.fields['anexo'].required = True
        self.fields['relacaoInterna'].required = True
        self.fields['relacaoExterna'].required = True
        self.fields['informacaoOutrosDocumentos'].required = True


    class Meta:
        model = Tipologia

        fields = ['producaoSetor', 'especieDocumental', 'finalidade', 'nome', 'identificacao', 'atividade',
                  'elemento', 'suporte', 'formaDocumental','quantidadeVias', 'genero', 'anexo', 'relacaoInterna', 'relacaoExterna',
                  'inicioAcumulo', 'fimAcumulo','quantidadeAcumulada','tipoAcumulo', 'embasamentoLegal',
                  'informacaoOutrosDocumentos', 'restricaoAcesso']

        labels = {
            'atividade':'Este documento está relacionado a qual atividade do setor?',
            'producaoSetor':'Este documento é:',
            'especieDocumental':'Espécie documental:',
            'identificacao':'Identificações no documento:',
            'formaDocumental':'Forma documental:',
            'elemento':'Marque os itens presentes neste documento:',
            'suporte':'Em qual suporte a informação circula?',
            'anexo':'Este documento pussui anexo?',
            'genero':'Qual o gênero predominante do documento?',
            'nome':'Nome do documento:',
            'finalidade':'Ação que gerou este documento / Objetivo para o qual foi produzido:',
            'relacaoInterna':'Este documento será encaminhado para outros setores?',
            'relacaoExterna':'Este documento será encaminhado para algum órgão externo ao Ifes?',
            'inicioAcumulo':'Qual o período de abrangência deste tipo de documento?',
            'quantidadeAcumulada':'Qual a quantidade e a forma de armazenamento deste documento?',
            'quantidadeVias':'Produz mais de uma via deste documento?',
            'embasamentoLegal':'Embasamento Legal:',
            'informacaoOutrosDocumentos':'Informações registradas em outros documentos:',
            'restricaoAcesso':'O documento contém informações que necessitam de restrição de acesso?',
        }

        help_texts={

            'nome':'Dica: Nome utilizado pelo setor para identificar o documento (Ex.: Folha de Ponto; Relatório de Atividades).',
            'identificacao':'Dica: Números e siglas presentes no documento (Ex.: Mem. nº 006-2016-DACV)',
            'embasamentoLegal':'Dica: Existe alguma normativa ou legislação específica sobre a configuração (Boletim, certidão, etc) que este documento possui e o conteúdo tratado nele?',
            'informacaoOutrosDocumentos':'Dica: As informações que estão neste documento encontram-se também em outros? (Ex: relatórios parciais que têm suas informações compiladas em um relatório final)',
        }

        # widgets={
        #     'elemento':SelectMultiple(attrs={'class':'browser-default selectField'}),
        # }

class FormUser(ModelForm):
    first_name = forms.CharField(label='Nome', max_length=30)
    last_name = forms.CharField(label='Sobrenome', max_length=30)
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'username': TextInput(attrs={'id':'id-username'}),
            'password':TextInput(attrs={'id':'id-password', 'type':'password'}),

        }
        labels = {
            'username': ('SIAPE:'),
            'password': ('Senha:'),

        }
        help_texts={
            'username':'',
        }

class FormParcialSetor(ModelForm):
    class Meta:
        model = Setor
        exclude = ['nome', 'sigla', 'funcao', 'historico']
        widgets = {
            'campus': Select(attrs={'id':'id-campus','class':'browser-default selectField'})
                    }


class FormUsuario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['setor']
        widgets = {
            'setor': Select(attrs={'id':'id-setor','class':'browser-default selectField'}),
        }
