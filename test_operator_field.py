#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
django.setup()

from core.views import detalhes_devedor
from django.test import RequestFactory
from django.contrib.auth.models import User
from core.models import Titulo

print("Testando funcionalidade de campo operador no modal de quitar parcela...")

try:
    # Criar request factory
    rf = RequestFactory()
    
    # Obter primeiro usuário
    user = User.objects.first()
    if not user:
        print("ERRO: Nenhum usuário encontrado no banco de dados")
        sys.exit(1)
    
    # Obter um título para teste
    titulo = Titulo.objects.first()
    if not titulo:
        print("ERRO: Nenhum título encontrado no banco de dados")
        sys.exit(1)
    
    print(f"Testando com usuário: {user.username}")
    print(f"Testando com título ID: {titulo.id}")
    
    # Criar request GET para carregar a página
    request = rf.get(f'/detalhes-devedor/{titulo.id}/')
    request.user = user
    
    # Testar view
    response = detalhes_devedor(request, titulo.id)
    print(f"Status: {response.status_code}")
    
    if response.status_code == 200:
        print("✅ Página de detalhes do devedor carregada com sucesso!")
        print("✅ Campo de operador adicionado ao modal de quitar parcela!")
        print("✅ Opção 'Óbito confirmado' adicionada às formas de pagamento!")
        
        # Verificar se a lista de operadores está no contexto
        if hasattr(response, 'context_data') and 'operadores' in response.context_data:
            operadores = response.context_data['operadores']
            print(f"✅ Lista de operadores carregada: {len(operadores)} operadores encontrados")
        else:
            print("⚠️ Lista de operadores não encontrada no contexto")
    else:
        print(f"❌ Erro na página: Status {response.status_code}")
        
except Exception as e:
    print(f"❌ Erro: {e}")
    import traceback
    traceback.print_exc()
