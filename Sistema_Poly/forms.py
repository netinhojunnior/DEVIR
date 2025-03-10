from django import forms
from .models import Fase1, Fase2, Fase3, Fase4

class Fase1Form(forms.ModelForm):
    class Meta:
        model = Fase1
        fields = '__all__'  # Inclui todos os campos do modelo

# Fase 2 ---------------------------------------------------------------------------------------------------------------
class Fase2Form(forms.ModelForm):
    class Meta:
        model = Fase2
        fields = '__all__'

    def clean_data_atendimento_fase2(self):
        # Podemos implementar um validador para garantir que a data esteja no formato certo
        return self.cleaned_data['data_atendimento_fase2']

# Fase 3 ---------------------------------------------------------------------------------------------------------------
class Fase3Form(forms.ModelForm):
    class Meta:
        model = Fase3
        fields = '__all__'

    def clean_como_soube(self):
        como_soube = self.cleaned_data.get('como_soube')

        if isinstance(como_soube, list):
            # Se for uma lista (múltiplos valores), junte com ";"
            return ";".join(como_soube)
        return como_soube

    def clean_medidas_protetivas(self):
        medidas = self.cleaned_data.get('medidas_protetivas')

        if isinstance(medidas, list):
            # Se for uma lista (múltiplos valores), junte com ";"
            return ";".join(medidas)
        return medidas

    def clean_agressao_fisica(self):
        agressao_fisica = self.cleaned_data.get('agressao_fisica')

        if isinstance(agressao_fisica, list):
            # Se for uma lista (múltiplos valores), junte com ";"
            return ";".join(agressao_fisica)
        return agressao_fisica

    def clean_comportamentos(self):
        comportamentos = self.cleaned_data.get('comportamentos')

        if isinstance(comportamentos, list):
            # Se for uma lista (múltiplos valores), junte com ";"
            return ";".join(comportamentos)
        return comportamentos

    def clean_agressao_outros(self):
        agressao_outros = self.cleaned_data.get('agressao_outros')

        if isinstance(agressao_outros, list):
            # Se for uma lista (múltiplos valores), junte com ";"
            return ";".join(agressao_outros)
        return agressao_outros

    def clean_motivos_retorno(self):
        motivos_retorno = self.cleaned_data.get("motivos_retorno")

        if isinstance(motivos_retorno, list):
            return ";".join(motivos_retorno)  # Une os dados com ";"
        return motivos_retorno

# Fase 4 ---------------------------------------------------------------------------------------------------------------
class Fase4Form(forms.ModelForm):
    class Meta:
        model = Fase4
        fields = '__all__'

    def clean_data_atendimento_fase4(self):
        # Apenas retorna o valor do campo sem aplicar validação extra
        return self.cleaned_data['data_atendimento_fase4']

# Formulário de Busca --------------------------------------------------------------------------------------------------

class BuscaForm(forms.Form):
    protocolo = forms.CharField(required=False, max_length=50)
    nome = forms.CharField(required=False, max_length=255)
    fase = forms.ChoiceField(required=False, choices=[("", "Selecione"),
                                                      ("Fase 1", "Fase 1"),
                                                      ("Fase 2", "Fase 2"),
                                                      ("Fase 3", "Fase 3"),
                                                      ("Fase 4", "Fase 4")]
                             )
    status = forms.ChoiceField(required=False, choices=[("", "Selecione"),
                                                        ("Em Andamento", "Em Andamento"),
                                                        ("Concluída", "Concluída"),
                                                        ("Desistência", "Desistência")]
                               )