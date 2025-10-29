from django.urls import path, include
from . import views
from .views import listar_devedores, listar_titulos_por_devedor, adicionar_devedor, editar_devedor, excluir_devedor, realizar_acordo, reparcelar_acordo, listar_acordos, pagar_parcela, detalhar_parcela, listar_empresas, adicionar_empresa, editar_empresa, excluir_empresa, consultar_cnpj_view,  gerar_contrato, anexar_contrato, baixar_contrato_view, gerar_contrato_lojista, gerar_ficha_lojista, buscar_dados_api_cliente, editar_titulo, alterar_status_empresa,  buscar_devedores, proximo_cliente
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler403, static
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
import base64


 
handler403 = 'core.views.permission_denied_view'



urlpatterns = [
    path('', views.home_redirect, name='home'),  # Rota para redirecionar para o dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assumir-devedor/<int:titulo_id>/', views.assumir_devedor, name='assumir_devedor'),
    path('devedores/listar/', listar_devedores, name='devedores_listar'),
    path("titulos/<int:titulo_id>/anexos.json", views.titulo_anexos_json, name="titulo_anexos_json"),
    path('agendamentos/cadastrar/', views.agendamentos_cadastrar, name='agendamentos_cadastrar'),       
    path('devedores/', views.listar_devedores, name='listar_devedores'),
    path('devedores/adicionar/', views.adicionar_devedor, name='adicionar_devedor'),
    path('devedores/<int:id>/editar/', editar_devedor, name='editar_devedor'),
    path('devedores/<int:id>/excluir/', excluir_devedor, name='excluir_devedor'),
    path('devedores/<int:devedor_id>/titulos/', listar_titulos_por_devedor, name='listar_titulos_por_devedor'),
    path('devedores/<int:devedor_id>/titulos/', views.listar_titulos_por_devedor, name='titulos_listar_por_devedor'),
    path('titulos/', views.titulos_listar, name='titulos_listar'),
    path('titulos/adicionar/', views.adicionar_titulo, name='adicionar_titulo'),
    path('titulos/<int:id>/editar/', views.editar_titulo, name='editar_titulo'),
    path('titulos/<int:id>/excluir/', views.excluir_titulo, name='excluir_titulo'),
    path('login/', views.login_view, name='login'),
    path("titulos/<int:titulo_id>/comprovante/", views.anexar_comprovante_titulo, name="anexar_comprovante_titulo"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/consultar-devedor/', views.consult_api, name='consult_api'),
    path('titulos/<int:titulo_id>/acordo/', views.realizar_acordo, name='realizar_acordo'),    
    path('acordos/<int:titulo_id>/reparcelar/', views.reparcelar_acordo, name='reparcelar_acordo'),
    path('acordos/listar/', views.listar_acordos, name='acordos_listar'),
    path('parcelamentos/', views.listar_parcelamentos, name='listar_parcelamentos'),
    path('parcelamentos/pagar/<int:parcela_id>/', pagar_parcela, name='pagar_parcela'), 
    path('empresas/', views.listar_empresas, name='listar_empresas'),
    path('titulos/<int:titulo_id>/baixar/', views.realizar_baixa, name='realizar_baixa'),
    path('devedores/<int:devedor_id>/adicionar-titulo/', views.adicionar_titulo_pg_devedor, name='adicionar_titulo_pg_devedor'),
    path('agendamentos/', views.listar_agendamentos, name='listar_agendamentos'),
    path('agendamentos/criar/', views.criar_agendamento, name='criar_agendamento'),
    path('agendamentos/<int:agendamento_id>/editar/', views.editar_agendamento, name='editar_agendamento'),
    path('agendamentos/<int:agendamento_id>/excluir/', views.excluir_agendamento, name='excluir_agendamento'),
    path('agendamentos/finalizar/<int:agendamento_id>/', views.finalizar_agendamento, name='finalizar_agendamento'),
     path('parcelamentos/<int:parcelamento_id>/', detalhar_parcela, name='detalhar_parcela'),
     path('detalhes-devedor/<int:titulo_id>/', views.detalhes_devedor, name='detalhes_devedor'),

     path('editar-telefones/<int:devedor_id>/', views.editar_telefones, name='editar_telefones'),
       path('lista-titulos/', views.lista_titulos, name='lista_titulos'),
       path('empresas/', listar_empresas, name='listar_empresas'),
    path('empresas/adicionar/', adicionar_empresa, name='adicionar_empresa'),
    path('empresas/<int:id>/editar/', editar_empresa, name='editar_empresa'),
    path('empresas/<int:id>/excluir/', excluir_empresa, name='excluir_empresa'),
    path('empresas/consultar_cnpj/', consultar_cnpj_view, name='consultar_cnpj'),
    path('titulos/<int:titulo_id>/gerar_pdf/', views.gerar_pdf, name='gerar_pdf'),
    path("baixar_modelo_devedor/", views.baixar_modelo_devedor, name="baixar_modelo_devedor"),
    path("importar_devedor/", views.importar_devedor, name="importar_devedor"),
    path('gerar-recibo/<int:titulo_id>/', views.gerar_recibo, name='gerar_recibo'),
    path('acordos/<int:titulo_id>/gerar_contrato/', views.gerar_contrato, name='gerar_contrato'),
    path('adicionar-follow-up/<int:devedor_id>/', views.adicionar_follow_up, name='adicionar_follow_up'),
    path('listar-follow-ups/<int:devedor_id>/', views.listar_follow_ups, name='listar_follow_ups'),
    path('logs/', views.listar_logs, name='listar_logs'),    
    path('parcelamento/<int:parcela_id>/anexar-comprovante/', views.anexar_comprovante, name='anexar_comprovante'),
    path('baixar_comprovante/<int:parcelamento_id>/', views.baixar_comprovante, name='baixar_comprovante'),
    path('mensagens/', views.listar_mensagens, name='listar_mensagens'),    
    path('mensagens/adicionar/', views.adicionar_mensagem, name='adicionar_mensagem'),
    path('mensagens/editar/<int:pk>/', views.editar_mensagem, name='editar_mensagem'),
    path('mensagens/excluir/<int:pk>/', views.excluir_mensagem, name='excluir_mensagem'),
  
     path('finalizar-titulo/<int:titulo_id>/', views.finalizar_titulo, name='finalizar_titulo'),
     path('quitar-parcela/<int:titulo_id>/', views.quitar_parcela, name='quitar_parcela'),
     path('extornar-parcela/<int:titulo_id>/', views.extornar_parcela, name='extornar_parcela'),

     
     #Anexar e baixar contrato
     path('anexar-contrato/<int:titulo_id>/', views.anexar_contrato, name='anexar_contrato'),
     
    path('baixar-contrato/<int:titulo_id>/', views.baixar_contrato_view, name='baixar_contrato'),
    
    
    #Gerar contrato lojista, tela  lista empresas/
    path('empresas/<int:id>/gerar_contrato_lojista/', gerar_contrato_lojista, name='gerar_contrato_lojista'),
    
    #Gerar ficha lojista, tela  lista empresas/
    path('empresas/<int:id>/gerar_ficha_lojista/', views.gerar_ficha_lojista, name='gerar_ficha_lojista'),
    
    path('devedores/<int:devedor_id>/busca_dados_api_cliente/', buscar_dados_api_cliente, name='buscar_dados_api_cliente'),
    
    path('salvar_dados_api_cadastro/', views.salvar_dados_api_cadastro, name='salvar_dados_api_cadastro'),
     
     path('titulos/<int:id>/editar/', views.editar_titulo, name='editar_titulo'),
      path('empresa/alterar_status/<int:id>/', alterar_status_empresa, name='alterar_status_empresa'),
    
    path('agendamentos/buscar_devedores/', buscar_devedores, name='buscar_devedores'),
    path('consult-api/', views.consult_api, name='consult_api'),
    path('devedores/proximo/<int:titulo_id>/', views.proximo_cliente, name='proximo_cliente'),
    path('iniciar-cobrancas/', views.iniciar_cobrancas, name='iniciar_cobrancas'),


   





]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   
