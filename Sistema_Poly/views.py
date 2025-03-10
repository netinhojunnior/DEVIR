from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Fase1, Fase2, Fase3, Fase4
from .forms import Fase1Form, Fase2Form, Fase3Form, Fase4Form


def menu(request):
    return render(request, 'atendimentos/menu.html')

def sub_menu(request):
    option = request.GET.get('option', None)

    if option == 'realizar_atendimento':
        submenu = ['Iniciar Fase 1', 'Iniciar Fase 2', 'Iniciar Fase 3', 'Iniciar Fase 4']
    elif option == 'ver_casos':
        submenu = ['Função a ser implementada']
    else:
        submenu = []

    return render(request, 'atendimentos/sub_menu.html', {'submenu': submenu, 'option': option})

# Função para exibir e processar o formulário da Fase 1
def fase1_view(request):
    if request.method == 'POST':
        form = Fase1Form(request.POST, request.FILES)  # Não esquecer de incluir request.FILES
        if form.is_valid():
            form.save()  # Salva os dados no banco
            print("Formulário salvo com sucesso!")  # Verifique no console
            return redirect('Sistema_Poly:tela_de_sucesso_fase1')  # Redireciona para a página de sucesso
        else:
            print("Formulário inválido. Erros:", form.errors)  # Exibe erros no console
    else:
        form = Fase1Form()  # Cria o formulário vazio para GET

    return render(request, 'atendimentos/fase1_form.html', {'form': form})

def fase2_view(request):
    if request.method == 'POST':
        form = Fase2Form(request.POST)
        if form.is_valid():
            form.save()  # Isso salva os dados no banco de dados
            messages.success(request, "Dados da Fase 2 cadastrados com sucesso!")
            return redirect('Sistema_Poly:tela_de_sucesso_fase2')  # Redireciona para a página de cadastro
        else:
            messages.error(request, "Erro ao cadastrar os dados. Verifique os campos.")
            print(form.errors)  # Isso vai imprimir os erros no console para você verificar
    else:
        form = Fase2Form()

    return render(request, 'atendimentos/fase2_form.html', {'form': form})


def fase3_view(request):
    if request.method == 'POST':
        form = Fase3Form(request.POST)

        if form.is_valid():
            try:
                # Pega as medidas protetivas selecionadas
                medidas_selecionadas = request.POST.getlist('medidas_protetivas[]')
                agressoes_selecionadas = request.POST.getlist('agressao_fisica[]')
                comportamentos_selecionados = request.POST.getlist('comportamentos[]')
                agressao_outros_selecionados = request.POST.getlist('agressao_outros[]')
                como_soube_selecionados = request.POST.getlist('como_soube[]')
                motivos_retorno_selecionados = request.POST.getlist('motivos_retorno[]')

                # Cria a instância do objeto e salva as medidas
                fase3 = form.save(commit=False)

                fase3.set_medidas_protetivas(medidas_selecionadas)
                fase3.set_agressao_fisica(agressoes_selecionadas)
                fase3.set_comportamentos(comportamentos_selecionados)
                fase3.set_agressao_outros(agressao_outros_selecionados)
                fase3.set_como_soube(como_soube_selecionados)
                fase3.set_motivos_retorno(motivos_retorno_selecionados)

                fase3.save()  # Salva o objeto no banco de dados

                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('Sistema_Poly:tela_de_sucesso_fase3')
            except Exception as e:
                messages.error(request, f'Ocorreu um erro ao salvar os dados: {e}')
                print(f'Erro ao salvar Fase3: {e}')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
            print(form.errors)
    else:
        form = Fase3Form()

    return render(request, 'atendimentos/fase3_form.html', {'form': form})

def fase4_view(request):
    if request.method == 'POST':
        form = Fase4Form(request.POST)
        if form.is_valid():
            form.save()  # Aqui é onde os dados são salvos
            messages.success(request, "Dados da Fase 4 cadastrados com sucesso!")
            return redirect('Sistema_Poly:tela_de_sucesso_fase4')  # Redirecionamento após o sucesso
        else:
            # Exibindo os erros de validação
            messages.error(request, "Erro ao cadastrar os dados. Verifique os campos.")
            print(form.errors)  # Aqui você verá os erros de validação
    else:
        form = Fase4Form()

    return render(request, 'atendimentos/fase4_form.html', {'form': form})

# Telas de Sucesso -----------------------------------------------------------------------------------------------------
def sucesso_fase1(request):
    return render(request, 'atendimentos/tela_de_sucesso_fase1.html')

def sucesso_fase2(request):
    return render(request, 'atendimentos/tela_de_sucesso_fase2.html')

def sucesso_fase3(request):
    return render(request, 'atendimentos/tela_de_sucesso_fase3.html')
def sucesso_fase4(request):
    return render(request, 'atendimentos/tela_de_sucesso_fase4.html')

def informativo(request):
    return render(request, 'atendimentos/informativo.html')

def atualiza_tela_sucesso_fase1(request):
    return render(request, 'atendimentos/atualiza_tela_sucesso_fase1.html')

def atualiza_tela_sucesso_fase2(request):
    return render(request, 'atendimentos/atualiza_tela_sucesso_fase2.html')

def atualiza_tela_sucesso_fase3(request):
    return render(request, 'atendimentos/atualiza_tela_sucesso_fase3.html')

def atualiza_tela_sucesso_fase4(request):
    return render(request, 'atendimentos/atualiza_tela_sucesso_fase4.html')

# Função de Busca ------------------------------------------------------------------------------------------------------
import psycopg2

def busca_protocolos(request):
    protocolo = request.GET.get('protocolo', '')
    nome_vitima = request.GET.get('nome_vitima', '')
    fase = request.GET.get('fase', '')
    status_fase = request.GET.get('status_fase', '')

    try:
        # Conectando ao banco PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="Poly",
            user="postgres",
            password="123456"
        )
        cursor = conn.cursor()

        query = """
        SELECT 
            f1.protocolo, 
            f1.nome_completo, 
            COALESCE(f4.data_atendimento_fase4, f3.data_hora_fase3, f2.data_atendimento_fase2, f1.finalizacao_atendimento) AS data_ultimo_atendimento,
            COALESCE(f4.status_fase, f3.status_fase, f2.status_fase, f1.status_fase) AS status_fase,
            CASE 
                WHEN f4.status_fase IS NOT NULL THEN 'Fase 4'
                WHEN f3.status_fase IS NOT NULL THEN 'Fase 3'
                WHEN f2.status_fase IS NOT NULL THEN 'Fase 2'
                ELSE 'Fase 1'
            END AS fase_atual
        FROM public."Sistema_Poly_fase1" f1
        LEFT JOIN public."Sistema_Poly_fase2" f2 ON f1.protocolo = f2.protocolo
        LEFT JOIN public."Sistema_Poly_fase3" f3 ON f1.protocolo = f3.protocolo
        LEFT JOIN public."Sistema_Poly_fase4" f4 ON f1.protocolo = f4.protocolo
        WHERE TRUE
        """

        # Filtro opcional
        params = []
        if protocolo:
            query += " AND f1.protocolo = %s"
            params.append(protocolo)
        if nome_vitima:
            query += " AND f1.nome_completo ILIKE %s"
            params.append(f"%{nome_vitima}%")
        if fase:
            query += """
            AND CASE 
                    WHEN f4.status_fase IS NOT NULL THEN 'Fase 4'
                    WHEN f3.status_fase IS NOT NULL THEN 'Fase 3'
                    WHEN f2.status_fase IS NOT NULL THEN 'Fase 2'
                    ELSE 'Fase 1'
                END = %s
            """
            params.append(fase)
        if status_fase:
            query += " AND COALESCE(f4.status_fase, f3.status_fase, f2.status_fase, f1.status_fase) = %s"
            params.append(status_fase)

        # Executar a consulta SQL
        cursor.execute(query, params)
        results = cursor.fetchall()

    except (Exception, psycopg2.DatabaseError) as error:
        results = []
        print(f"Erro ao executar a consulta: {error}")
    finally:
        if conn:
            cursor.close()
            conn.close()

    return render(request, 'atendimentos/busca_form.html', {'resultados': results})

def detalhes_protocolo(request, protocolo):
    # Buscar as fases com o protocolo fornecido
    fase1 = Fase1.objects.filter(protocolo=protocolo).first()
    fase2 = Fase2.objects.filter(protocolo=protocolo).first()
    fase3 = Fase3.objects.filter(protocolo=protocolo).first()
    fase4 = Fase4.objects.filter(protocolo=protocolo).first()

    # Verificar se todas as fases foram encontradas
    if not any([fase1, fase2, fase3, fase4]):
        messages.error(request, "Protocolo não encontrado ou não tem fases associadas.")
        return render(request, 'atendimentos/detalhes_protocolo.html',
                      {'error': 'Protocolo não encontrado ou não tem fases associadas.'})

    # Inicializar os formulários para todas as fases
    form_fase1 = Fase1Form(instance=fase1)
    form_fase2 = Fase2Form(instance=fase2)
    form_fase3 = Fase3Form(instance=fase3)
    form_fase4 = Fase4Form(instance=fase4)

    # Se for um pedido POST (atualização dos dados)
    if request.method == 'POST':
        fase_selecionada = request.POST.get('fase')  # Captura a fase no formulário

        # Inicializar os formulários com os dados de request.POST apenas para a fase selecionada
        if fase_selecionada == 'fase1':
            form_fase1 = Fase1Form(request.POST, request.FILES, instance=fase1)
        elif fase_selecionada == 'fase2':
            form_fase2 = Fase2Form(request.POST, instance=fase2)
        elif fase_selecionada == 'fase3':
            form_fase3 = Fase3Form(request.POST, instance=fase3)
        elif fase_selecionada == 'fase4':
            form_fase4 = Fase4Form(request.POST, instance=fase4)

        # Verificar se o formulário da fase selecionada é válido e salvar
        if fase_selecionada == 'fase1' and form_fase1.is_valid():
            form_fase1.save()
            messages.success(request, "Fase 1 atualizada com sucesso.")
            return redirect('Sistema_Poly:atualiza_tela_sucesso_fase1')  # Redireciona para a tela de sucesso da fase 1

        elif fase_selecionada == 'fase2' and form_fase2.is_valid():
            form_fase2.save()
            messages.success(request, "Fase 2 atualizada com sucesso.")
            return redirect('Sistema_Poly:atualiza_tela_sucesso_fase2')  # Redireciona para a tela de sucesso da fase 2

        elif fase_selecionada == 'fase3' and form_fase3.is_valid():
            form_fase3.save()
            messages.success(request, "Fase 3 atualizada com sucesso.")
            return redirect('Sistema_Poly:atualiza_tela_sucesso_fase3')  # Redireciona para a tela de sucesso da fase 3

        elif fase_selecionada == 'fase4' and form_fase4.is_valid():
            form_fase4.save()
            messages.success(request, "Fase 4 atualizada com sucesso.")
            return redirect('Sistema_Poly:atualiza_tela_sucesso_fase4')  # Redireciona para a tela de sucesso da fase 4

        else:
            # Se algum formulário não for válido, exibir uma mensagem de erro
            messages.error(request, "Por favor, corrija os erros no formulário.")

    # Renderiza o template com os formulários e os dados das fases
    return render(request, 'atendimentos/detalhes_protocolo.html', {
        'fase1': fase1,
        'fase2': fase2,
        'fase3': fase3,
        'fase4': fase4,
        'protocolo': protocolo,
        'form_fase1': form_fase1,
        'form_fase2': form_fase2,
        'form_fase3': form_fase3,
        'form_fase4': form_fase4
    })