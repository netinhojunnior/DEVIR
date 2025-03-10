from django.db import models

class Fase1(models.Model):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    idade = models.IntegerField(null=True, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    bairro = models.CharField(max_length=255, blank=True)
    cidade = models.CharField(max_length=255, blank=True)
    estado = models.CharField(max_length=2, blank=True)
    protocolo = models.CharField(max_length=17, unique=True)
    validacao_dev = models.DateTimeField(null=True, blank=True)
    policial_validacao = models.CharField(max_length=255, blank=True)
    registro_comunicacao = models.DateTimeField(null=True, blank=True)
    data_fato = models.DateTimeField(null=True, blank=True)
    natureza = models.CharField(max_length=255, blank=True)
    dp_apuracao = models.CharField(max_length=255, blank=True)
    finalizacao_atendimento = models.DateTimeField(null=True, blank=True)
    policial_finalizacao = models.CharField(max_length=255, null=True, blank=True)
    status_fase = models.CharField(max_length=255, blank=True)
    falta_contato = models.CharField(max_length=255, null=True, blank=True)
    vitima_representou = models.CharField(max_length=255, null=True, blank=True)
    vitima_rep_criminal = models.CharField(max_length=255, null=True, blank=True)
    caso_piloto = models.CharField(max_length=255, null=True, blank=True)
    observacoes = models.TextField(null=True, blank=True)
    documentos = models.FileField(upload_to='documentos/', null=True, blank=True)

    def __str__(self):
        return f'{self.nome_completo} - {self.protocolo}'

# Fase 2 ---------------------------------------------------------------------------------------------------------------
class Fase2(models.Model):
    protocolo = models.CharField(max_length=17, unique=True, null=True)
    numero_bo = models.CharField(max_length=255, blank=True, null=True)
    data_atendimento_fase2 = models.DateTimeField(null=True, blank=True)
    policial_responsavel = models.CharField(max_length=155, blank=True, null=True)
    observacoes = models.TextField(null=True, blank=True)
    contato_vitima = models.CharField(max_length=255, blank=True, null=True)
    status_fase = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Fase 2 - Protocolo {self.protocolo} - {self.status_fase}"

# Fase 3 ---------------------------------------------------------------------------------------------------------------
class Fase3(models.Model):
    protocolo = models.CharField(max_length=17, unique=True, null=True)
    videoconferencia = models.CharField(max_length=255, blank=True, null=True)
    medidas_protetivas = models.TextField(blank=True, null=True)
    ameaca = models.CharField(max_length=255, blank=True, null=True)
    agressao_fisica = models.TextField(blank=True, null=True)
    atendimento_medico = models.CharField(max_length=255, blank=True, null=True)
    agressao_sexual = models.CharField(max_length=255, blank=True, null=True)
    agressao_controle = models.CharField(max_length=255, blank=True, null=True)
    comportamentos = models.CharField(max_length=255, blank=True, null=True)
    registro_ocorrencia = models.CharField(max_length=255, blank=True, null=True)
    descumprimento_medida = models.CharField(max_length=255, blank=True, null=True)
    numero_processo_mpu = models.CharField(max_length=255, blank=True, null=True)
    agressao_frequente = models.CharField(max_length=255, blank=True, null=True)
    uso_abusivo = models.CharField(max_length=255, blank=True, null=True)
    doenca_mental = models.CharField(max_length=255, blank=True, null=True)
    suicidio = models.CharField(max_length=255, blank=True, null=True)
    dificuldade_financeira = models.CharField(max_length=255, blank=True, null=True)
    arma_fogo = models.CharField(max_length=255, blank=True, null=True)
    agressao_outros = models.CharField(max_length=500, blank=True, null=True)
    separacao_recente = models.CharField(max_length=255, blank=True, null=True)
    qtd_filhos = models.CharField(max_length=255, blank=True, null=True)
    filhos_com_agressor = models.CharField(max_length=255, blank=True, null=True)
    filho_com_deficiencia = models.CharField(max_length=255, blank=True, null=True)
    conflito_guarda = models.CharField(max_length=255, blank=True, null=True)
    filhos_presenciaram = models.CharField(max_length=255, blank=True, null=True)
    violencia_gravidez = models.CharField(max_length=255, blank=True, null=True)
    gravida_ou_bebe = models.CharField(max_length=255, blank=True, null=True)
    ameacas_novo_relacionamento = models.CharField(max_length=255, blank=True, null=True)
    deficiencia_ou_doenca = models.CharField(max_length=255, blank=True, null=True)
    deficiencia_vitima = models.CharField(max_length=255, blank=True, null=True)
    cor_raca = models.CharField(max_length=255, blank=True, null=True)
    bairro_comunidade_rural = models.CharField(max_length=255, blank=True, null=True)
    situacao_moradia = models.CharField(max_length=255, blank=True, null=True)
    moradia_cedida = models.CharField(max_length=255, blank=True, null=True)
    dependente_financeiramente = models.CharField(max_length=255, blank=True, null=True)
    abrigamento_temporario = models.CharField(max_length=255, blank=True, null=True)
    informacoes_beneficios = models.CharField(max_length=255, blank=True, null=True)
    dependentes_nome_idade = models.CharField(max_length=255, blank=True, null=True)
    natureza_dos_crimes = models.CharField(max_length=255, blank=True, null=True)
    advogado_ou_defensor = models.CharField(max_length=255, blank=True, null=True)
    como_soube = models.CharField(max_length=255, blank=True, null=True)
    delegacia_busca_informacao = models.CharField(max_length=255, blank=True, null=True)
    especificar_delegacia = models.TextField(blank=True, null=True)
    ajuda_registro = models.CharField(max_length=255, blank=True, null=True)
    atendimento_psicologico = models.CharField(max_length=255, blank=True, null=True)
    telefone_endereco_whatsapp = models.TextField(blank=True, null=True)
    atendimento_medico_vitima = models.CharField(max_length=255, blank=True, null=True)
    reataram_relacionamento = models.CharField(max_length=255, blank=True, null=True)
    motivos_retorno = models.TextField(blank=True, null=True)
    agressao_relacionamento = models.CharField(max_length=255, blank=True, null=True)
    alteracao_informacoes = models.CharField(max_length=255, blank=True, null=True)
    data_hora_fase3 = models.DateTimeField(blank=True, null=True)
    policial_responsavel = models.CharField(max_length=255, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    status_fase = models.CharField(max_length=255, blank=True, null=True)

    # Separando medidas protetivas por ;
    def set_medidas_protetivas(self, medidas):
        # Junta as medidas com vírgulas
        self.medidas_protetivas = ";".join(medidas)

    def get_medidas_protetivas(self):
        # Converte a string de volta para uma lista
        if self.medidas_protetivas:
            return self.medidas_protetivas.split(";")
        return []

    # Separando agressões físicas por ;
    def set_agressao_fisica(self, agressao):
        # Junta as medidas com vírgulas
        self.agressao_fisica = ";".join(agressao)

    def get_agressao_fisica(self):
        # Converte a string de volta para uma lista
        if self.agressao_fisica:
            return self.agressao_fisica.split(";")
        return []

    # Separando comportamentos por ;
    def set_comportamentos(self, comportamentos):
        # Junta as medidas com vírgulas
        self.comportamentos = ";".join(comportamentos)

    def get_comportamentos(self):
        # Converte a string de volta para uma lista
        if self.comportamentos:
            return self.comportamentos.split(";")
        return []

    # Separando agressão a outros por ;
    def set_agressao_outros(self, agressao):
        # Junta as medidas com vírgulas
        self.agressao_outros = ";".join(agressao)

    def get_agressao_outros(self):
        # Converte a string de volta para uma lista
        if self.agressao_outros:
            return self.agressao_outros.split(";")
        return []

    # Separando informações de como soube por ;
    def set_como_soube(self, como_soube):
        # Junta as medidas com vírgulas
        self.como_soube = ";".join(como_soube)

    def get_como_soube(self):
        # Converte a string de volta para uma lista
        if self.como_soube:
            return self.como_soube.split(";")
        return []

    # Separando motivos do retorno por ;
    def set_motivos_retorno(self, motivos):
        # Junta as medidas com vírgulas
        self.motivos_retorno = ";".join(motivos)

    def get_motivos_retorno(self):
        # Converte a string de volta para uma lista
        if self.motivos_retorno:
            return self.motivos_retorno.split(";")
        return []

    def __str__(self):
        return self.protocolo

# Fase 4 ---------------------------------------------------------------------------------------------------------------
class Fase4(models.Model):
    protocolo = models.CharField(max_length=17, unique=True, null=True)
    data_atendimento_fase4 = models.DateTimeField(blank=True, null=True)
    policial_finalizacao_fase4 = models.CharField(max_length=255, blank=True, null=True)
    representou_crime = models.CharField(max_length=255, blank=True, null=True)
    agressao = models.CharField(max_length=255, blank=True, null=True)
    situacao_mpu = models.CharField(max_length=255, blank=True, null=True)
    data_concessao_mpu = models.DateField(null=True, blank=True)
    mpu_enviado_ao_tj = models.CharField(max_length=255, blank=True, null=True)
    numero_processo_protecao = models.CharField(max_length=255, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    status_fase = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Fase 4 - Protocolo {self.protocolo} - {self.status_fase}"

class Midia(models.Model):
    tipo_choices = [
        ('imagem', 'Imagem'),
        ('video', 'Vídeo'),
    ]
    arquivo = models.FileField(upload_to='midias/', blank=True, null=True)
    tipo = models.CharField(max_length=10, choices=tipo_choices, blank=True, null=True)
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.arquivo.name
