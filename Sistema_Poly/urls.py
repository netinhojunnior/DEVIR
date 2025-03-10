from django.urls import path
from . import views

app_name = 'Sistema_Poly'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('sub_menu/', views.sub_menu, name='sub_menu'),
    path('iniciar_fase1/', views.fase1_view, name='iniciar_fase1'),
    path('iniciar_fase2/', views.fase2_view, name='iniciar_fase2'),
    path('iniciar_fase3/', views.fase3_view, name='iniciar_fase3'),
    path('iniciar_fase4/', views.fase4_view, name='iniciar_fase4'),
    path('busca_protocolo/', views.busca_protocolos, name='busca_protocolos'),
    path('detalhes_protocolo/<path:protocolo>/', views.detalhes_protocolo, name='detalhes_protocolo'),
    path('tela_de_sucesso_fase1/', views.sucesso_fase1, name='tela_de_sucesso_fase1'),
    path('tela_de_sucesso_fase2/', views.sucesso_fase2, name='tela_de_sucesso_fase2'),
    path('tela_de_sucesso_fase3/', views.sucesso_fase3, name='tela_de_sucesso_fase3'),
    path('tela_de_sucesso_fase4/', views.sucesso_fase4, name='tela_de_sucesso_fase4'),
    path('atualiza_tela_sucesso_fase1/', views.atualiza_tela_sucesso_fase1, name='atualiza_tela_sucesso_fase1'),
    path('atualiza_tela_sucesso_fase2/', views.atualiza_tela_sucesso_fase2, name='atualiza_tela_sucesso_fase2'),
    path('atualiza_tela_sucesso_fase3/', views.atualiza_tela_sucesso_fase3, name='atualiza_tela_sucesso_fase3'),
    path('atualiza_tela_sucesso_fase4/', views.atualiza_tela_sucesso_fase4, name='atualiza_tela_sucesso_fase4'),
    path('informativo/', views.informativo, name='informativo'),
]